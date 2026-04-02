from fastapi import FastAPI
from app.pool import allocate_vm, release_vm, load_pool
from app.ansible_runner import run_playbook
from app.gitlab import get_merge_requests
from app.jenkins import trigger_build, get_last_successful_build, get_last_build_for_branch
import yaml
import os

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/merge-requests")
def merge_requests():
    return get_merge_requests()

@app.post("/start-test")
def start_test(user: str, branch_name: str):
    vm = allocate_vm(user, branch_name)
    run_playbook(vm, "playbook_startvm.yml")
    return {"vm": vm, "status": "starting vm"}

@app.post("/release")
def release(vm: str):
    run_playbook(vm, "playbook_stopvm.yml")
    release_vm(vm)
    return {"status": "released"}

@app.post("/deploy-build")
def deploy_build(user: str, branch_name: str):
    vm = allocate_vm(user, branch_name)
    run_playbook(vm, "playbook-deploy-build.yml", extra_vars={"branch_name": branch_name})
    return {"vm": vm, "status": "DEPLOYING_BUILD"}

@app.post("/trigger-build")
def trigger_build_endpoint(branch_name: str, quartals_version: str = "false"):
    status_code = trigger_build(branch_name, quartals_version)
    return {"status": "triggered", "jenkins_status_code": status_code}

@app.get("/last-successful-build")
def last_successful_build():
    description = get_last_successful_build()
    return {"description": description}

@app.get("/last-build-for-branch")
def last_build_for_branch(branch_name: str):
    return get_last_build_for_branch(branch_name)

@app.get("/ansiblehost")
def ansible_host(name: str):
    host_vars_path = os.path.join(os.path.dirname(__file__), "..", "ansible", "host_vars", f"{name}.yml")
    if not os.path.isfile(host_vars_path):
        return {"error": f"Host '{name}' not found"}
    with open(host_vars_path) as f:
        data = yaml.safe_load(f)
    return data

@app.get("/pool")
def pool_status():
    return load_pool()
