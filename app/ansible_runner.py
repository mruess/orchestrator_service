import subprocess
import os

def run_playbook(vm, playbook="playbook.yml", extra_vars=None):
    log_dir = os.path.join(os.path.dirname(__file__), "..", "log")
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, "ansible.log")
    cmd = [
        "ansible-playbook",
        playbook,
        "-i", "inventory/",
        "--vault-password-file", "./vault-pass.sh",
        "-l", vm,
    ]
    if extra_vars:
        for key, value in extra_vars.items():
            cmd.extend(["-e", f"{key}={value}"])
    with open(log_path, "a") as logfile:
        subprocess.Popen(cmd, cwd="ansible", stdout=logfile, stderr=logfile)