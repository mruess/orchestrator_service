---
agent: agent
description: Get my Orchestrator workspace ready
tools: ['execute/runInTerminal', 'read', 'search', 'todo']
---

Your goal is to successfully build and run the workspace as local development environment.

## Checklist
- [ ] prüfe ob die Datei `.env` im Root-Verzeichnis existiert, wenn nicht erstelle sie und füge die notwendigen Secrets hinzu
- [ ] run `uvicorn app.main:app --reload` in the terminal in the background to start the API
- [ ] run `npm run dev` in the folder `/frontend` to start the frontend
- [ ] open http://localhost:5173/ in the integrated browser to see the frontend
