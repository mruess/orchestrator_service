---
agent: agent
description: Get my Orchestrator workspace ready
tools: ['execute/runInTerminal', 'read', 'search', 'todo']
---

Your goal is to successfully build and run the workspace as local development environment.

## Checklist
- [ ] run `uvicorn app.main:app --reload` in the terminal in the background to start the API. Installiere keine requirements, da das bereits im Devcontainer gemacht wird
- [ ] run `npm run dev` in the folder `/frontend` to start the frontend. Installiere keine node modules, da das bereits im Devcontainer gemacht wird
- [ ] open http://localhost:5173/ in the integrated browser to see the frontend
