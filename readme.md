# ▶️ Orchestrator im DevContainer

Der Container selbst macht beim PostCreate "pip install -r requirements.txt", deshalb bei Erweiterungen einfach die requirements.txt ändern.

## Setup
In copilot /setup eingeben. Er fragt nach dem Vault Passwort und startet den Dev-Server. Dieser kann mit den Curl-Kommandos unten angesprochen werden

## ansible
Ansible wird bereits mit dem Devcontainer PostCreate installiert, mehr dazu in dem Unterverzeichnis **ansible**

ansible ignoriert ansible.cfg wenn es Schreibrechte für "other" gibt. Wenn es rum meckert dann rum dass es das vault nicht auf bekommt
[ERROR]: Attempting to decrypt but no vault secrets found
Passiert gerne bei DevContainern. WICHTIG chmod ist Käse weil dann VScode selbst nicht mehr rein schreiben kann, deswegen lieber --vault-password-file mitgeben


```
ansible-playbook -i inventory/ playbook-snapshot.yml --vault-password-file ./vault-pass.sh
```

Vault Passwort setzten: 

```
export ANSIBLE_VAULT_PASSWORD=
```

Wird vergessen das Vault-Passwort vorher zu setzen dann kommt der Fehler:
[ERROR]: Invalid vault password was provided from script (/workspaces/orchestrator_service/ansible/vault-pass.sh)


## Service starten

```
uvicorn app.main:app --reload
```


## 🌐 API testen

Start Test

```
curl -X POST "http://127.0.0.1:8000/start-test?user=max&mr_id=123"
```

Release VM

```
curl -X POST "http://127.0.0.1:8000/release?vm=win-test-01&mr_id=123"
```

Merge Requests abfragen

```
curl http://127.0.0.1:8000/merge-requests
```

Build auf Jenkins triggern

```
curl -X POST "http://127.0.0.1:8000/trigger-build?branch_name=develop"
```

## benötigtes Environment für Jenkins und Gitlab
in /.env befinden sich die Secrets, diese Datei ist .gitignore und darf NICHT!!! comitted werden
Diese env Variblen werden beim Start von Docker oder des DevContainers automatisch geladen
ein Beispiel ist in .env.example

