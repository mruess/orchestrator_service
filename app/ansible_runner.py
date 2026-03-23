import subprocess

def run_playbook(vm, mr_id):
    cmd = [
        "ansible-playbook",
        "../ansible/playbook.yml",
        "-l", vm,
        "-e", f"mr_id={mr_id}"
    ]
    subprocess.Popen(cmd)
