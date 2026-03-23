▶️ Schnellstart
````
cd test_orchestrator_service
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
`````

🌐 API testen
Start Test
```
curl -X POST "http://127.0.0.1:8000/start-test?user=max&mr_id=123"
```
Release VM
curl -X POST "http://127.0.0.1:8000/release?vm=win-test-01"
