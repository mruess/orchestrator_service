import { useState, useEffect } from 'react'
import './App.css'

const API_URL = '/api/merge-requests'

function App() {
  const [mergeRequests, setMergeRequests] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetch(API_URL)
      .then((res) => {
        if (!res.ok) throw new Error(`HTTP ${res.status}`)
        return res.json()
      })
      .then((data) => {
        setMergeRequests(data)
        setLoading(false)
      })
      .catch((err) => {
        setError(err.message)
        setLoading(false)
      })
  }, [])

  return (
    <div className="app">
      <h1>Orchestrator</h1>

      {loading && <p>Lade Merge Requests…</p>}
      {error && <p className="error">Fehler: {error}</p>}

      {!loading && !error && (
        <div className="mr-list">
          <div className="mr-actions">
            <button className="btn btn-primary">Version erstellen</button>
            <button className="btn btn-secondary">Test</button>
          </div>

          <table>
            <thead>
              <tr>
                <th>Title</th>
                <th>Source Branch</th>
              </tr>
            </thead>
            <tbody>
              {mergeRequests.map((mr) => (
                <tr key={mr.id} data-id={mr.id}>
                  <td><a href={mr.web_url} target="_blank" rel="noopener noreferrer">{mr.title}</a></td>
                  <td><code>{mr.source_branch}</code></td>
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
