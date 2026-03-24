▶️ Schnellstart im DevContainer

Der Container selbst macht beim PostCreate "pip install -r requirements.txt", deshalb bei Erweiterungen einfach die requirements.txt ändern.


Service starten

```
uvicorn app.main:app --reload
```


🌐 API testen

Start Test

```
curl -X POST "http://127.0.0.1:8000/start-test?user=max&mr_id=123"
```

Release VM

```
curl -X POST "http://127.0.0.1:8000/release?vm=win-test-01"
```
