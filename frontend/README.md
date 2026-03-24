# Orchestrator Frontend

Web-Frontend für den Orchestrator Service. Zeigt offene GitLab Merge Requests als Liste an und bietet Aktionen wie „Version erstellen" und „Test".

## Technologie-Stack

- **React** 19 (JavaScript)
- **Vite** 8 als Build-Tool und Dev-Server
- **ESLint** für Code-Qualität

## Projektstruktur

```
frontend/
├── index.html            # HTML-Einstiegspunkt
├── package.json
├── vite.config.js        # Vite-Konfiguration
├── eslint.config.js
├── public/               # Statische Assets
└── src/
    ├── main.jsx          # React-Einstiegspunkt
    ├── App.jsx           # Haupt-Komponente (Merge Request Liste)
    ├── App.css           # Styles für App-Komponente
    ├── index.css         # Globale Styles
    └── assets/           # Bilder, Icons etc.
```

## Voraussetzungen

- **Node.js** >= 18
- **npm** (wird mit Node.js mitgeliefert)

## Installation

```bash
cd frontend
npm install
```

## Entwicklung

Dev-Server starten (mit Hot Module Replacement):

```bash
npm run dev
```

Der Server läuft standardmäßig auf `http://localhost:5173/`.

## API-Anbindung

Die App ruft Merge Requests vom Backend ab:

```
GET http://127.0.0.1:8080/merge-requests
```

Das Backend muss laufen, damit die Liste geladen wird.

## Build

Produktions-Build erstellen:

```bash
npm run build
```

Die gebauten Dateien landen in `dist/`.

## Vorschau des Builds

Den Produktions-Build lokal testen:

```bash
npm run preview
```

## Linting

Code-Qualität prüfen:

```bash
npm run lint
```
