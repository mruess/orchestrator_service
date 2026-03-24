---
agent: agent
description: Get my Orchestrator workspace ready
tools: ['execute/runInTerminal', 'read', 'search', 'todo']
---

Your goal is to successfully build and run the workspace as local development environment.

## Checklist
- [ ] ask the user for the password to the vault
- [ ] set the vault password as environment variable `ANSIBLE_VAULT_PASSWORD`
- [ ] run `uvicorn app.main:app --reload` in the terminal in the background to start the API
