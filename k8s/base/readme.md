Das sind alle Dateien die du brauchst. Was du noch anpassen musst:

`ghcr.io/DEIN-USER/DEIN-REPO/...` in den Deployments durch deine echten Image-Pfade ersetzen
`deine-app.example.com` im Ingress anpassen
Das `orchestrator-env` Secret muss im gleichen Namespace wie die Deployments liegen

Deployen:

```
bashkubectl apply -k k8s/base/
```

Dateistruktur:
k8s/
├── base/
│   ├── kustomization.yaml
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   └── ingress.yaml
└── overlays/
    └── production/
        └── kustomization.yaml


Traefik läuft – das ist k3s Standard. Gut, dann passen wir die Ingress-Annotations entsprechend an.

