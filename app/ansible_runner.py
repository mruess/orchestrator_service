import subprocess

# 1. Ruft ansible-playbook auf und begrenzt die Ausführung mit -l auf die angegebene VM.
# 2. Übergibt die mr_id (Merge-Request-ID) als Extra-Variable (-e), die dann im Playbook verfügbar ist.
# 3. Kehrt sofort zurück, ohne auf das Ergebnis zu warten — das Playbook läuft im Hintergrund weiter.

def run_playbook(vm, mr_id, playbook="../ansible/playbook.yml"):
    cmd = [
        "ansible-playbook",
        playbook,
        "-l", vm,
        "-e", f"mr_id={mr_id}"
    ]
    subprocess.Popen(cmd)
