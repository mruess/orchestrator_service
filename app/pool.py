import json
from pathlib import Path

POOL_FILE = Path("state/pool.json")

def load_pool():
    with open(POOL_FILE) as f:
        return json.load(f)

def save_pool(pool):
    with open(POOL_FILE, "w") as f:
        json.dump(pool, f, indent=2)

def allocate_vm(user, mr_id):
    pool = load_pool()
    for vm, data in pool.items():
        if data["status"] == "FREE":
            pool[vm] = {
                "status": "IN_USE",
                "user": user,
                "mr": mr_id
            }
            save_pool(pool)
            return vm
    raise Exception("No VM available")

def release_vm(vm):
    pool = load_pool()
    pool[vm] = {"status": "FREE"}
    save_pool(pool)
