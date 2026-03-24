import subprocess
import os

def run_playbook(vm, mr_id, playbook="playbook.yml"):
    log_dir = os.path.join(os.path.dirname(__file__), "..", "log")
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "ansible.log")
    cmd = [
        "ansible-playbook",
        playbook,
        "-i", "inventory/",
        "--vault-password-file", "./vault-pass.sh",
        "-l", vm,
        "-e", f"mr_id={mr_id}"
    ]
    with open(log_path, "a") as logfile:
        subprocess.Popen(cmd, cwd="ansible", stdout=logfile, stderr=logfile)