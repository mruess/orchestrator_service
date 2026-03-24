from fastapi import FastAPI
from app.pool import allocate_vm, release_vm
from app.ansible_runner import run_playbook

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.post("/start-test")
def start_test(user: str, mr_id: int):
    vm = allocate_vm(user, mr_id)
    run_playbook(vm, mr_id,"playbook_startvm.yml")
    return {"vm": vm, "status": "DEPLOYING"}

@app.post("/release")
def release(vm: str, mr_id: int):
    run_playbook(vm, mr_id,"playbook_stopvm.yml")
    release_vm(vm)
    return {"status": "released"}
