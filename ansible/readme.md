# Virtual environment installieren


## 🔧 Schritt 1: venv installieren (falls fehlt)

```
sudo apt update  
sudo apt install python3 -y 
sudo apt install python3-venv -y
```

---

## 📁 Schritt 2: Projekt-venv anlegen

In deinem Ansible-Ordner:

```
python3 -m venv .venv
```


## ▶️ Schritt 3: aktivieren

```
source .venv/bin/activate
```

👉 Danach siehst du sowas:

(.venv) user@wsl:~/ansible$   
Bei mir kommt da gar nichts, aber pip funktioniert hinterher....


Jetzt klappt pip wieder:

```
pip install proxmoxer requests
pip install pywinrm requests
```

---

## 🔧 Schritt 5: Ansible auch ins venv (empfohlen)

```
pip install ansible
ansible-galaxy collection install community.proxmox

```

👉 Vorteil:

- saubere Umgebung
- keine Konflikte mit System-Ansible

---

## 🚀 Nutzung danach

Immer vorher:

```
source .venv/bin/activate
```


## Ausführen

# einfacher test:

Ping an alle Testmaschinen. 


```
ansible all -i inventory/ -m win_ping
```

Ausgabe in der Art:

```
win-test-01 | SUCCESS => {
    "changed": false,
    "ping": "pong"
}
```
Mit Vault Passwort (ist wie immer)

export ANSIBLE_VAULT_PASSWORD=deinVaultPasswort
ansible-playbook playbook.yml





