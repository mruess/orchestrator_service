import { useState, useEffect } from 'react'
import './App.css'

const API_URL = '/api/merge-requests'

function App() {
  const [mergeRequests, setMergeRequests] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)
  const [lastBuild, setLastBuild] = useState(null)
  const [branchBuilds, setBranchBuilds] = useState({})

  const triggerBuild = async (mr) => {
    try {
      const res = await fetch(`/api/trigger-build?branch_name=${encodeURIComponent(mr.source_branch)}`, { method: 'POST' })
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      alert(`Build gestartet für Branch: ${mr.source_branch}`)
    } catch (err) {
      alert(`Fehler beim Build: ${err.message}`)
    }
  }

  const startTest = async (mr) => {
    try {
      const res = await fetch(`/api/start-test?mr_id=${mr.iid}`, { method: 'POST' })
      if (!res.ok) throw new Error(`HTTP ${res.status}`)
      alert(`Test gestartet für: ${mr.title}`)
    } catch (err) {
      alert(`Fehler beim Test: ${err.message}`)
    }
  }

  useEffect(() => {
    fetch('/api/last-successful-build')
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`)
        return res.json()
      })
      .then((data) => setLastBuild(data))
      .catch(() => setLastBuild(null))

    fetch(API_URL)
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`)
        return res.json()
      })
      .then((data) => {
        setMergeRequests(data)
        setLoading(false)

        const branches = [...new Set(data.map((mr) => mr.source_branch))]
        Promise.all(
          branches.map((branch) =>
            fetch(`/api/last-build-for-branch?branch_name=${encodeURIComponent(branch)}`)
              .then((res) => res.ok ? res.json() : null)
              .then((build) => [branch, build])
              .catch(() => [branch, null])
          )
        ).then((results) => {
          const builds = {}
          for (const [branch, build] of results) {
            if (build) builds[branch] = build
          }
          setBranchBuilds(builds)
        })
      })
      .catch((err) => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  return (
    <div className="app">
      <h1>Orchestrator</h1>

      {lastBuild && (
        <div className="card last-build-card">
          <h2>Letzter erfolgreicher Build</h2>
          <p>{lastBuild.description}</p>
        </div>
      )}

      {loading && <p>Lade Merge Requests…</p>}
      {error && <p className="error">Fehler: {error}</p>}

      {!loading && !error && (
        <div className="mr-list">
          <table>
            <thead>
              <tr>
                <th>Title</th>
                <th>Source Branch</th>
                <th>Letzter Build</th>
                <th>Aktionen</th>
              </tr>
            </thead>
            <tbody>
              {mergeRequests.map((mr) => (
                <tr key={mr.id} data-id={mr.id}>
                  <td><a href={mr.web_url} target="_blank" rel="noopener noreferrer">{mr.title}</a></td>
                  <td><code>{mr.source_branch}</code></td>
                  <td>{branchBuilds[mr.source_branch] ? `${new Date(branchBuilds[mr.source_branch].buildTime).toLocaleString('de-DE', { timeZone: 'Europe/Berlin' })} — ${branchBuilds[mr.source_branch].installer}` : '–'}</td>
                  <td className="row-actions">
                    <button className="btn btn-primary btn-sm" onClick={() => triggerBuild(mr)}>Version erstellen</button>
                    <button className="btn btn-secondary btn-sm" onClick={() => startTest(mr)}>Test</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  )
}

export default App
