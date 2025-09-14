# פרויקט דוגמה – FastAPI + Docker

המטרה: פרויקט גנרי ופשוט שאפשר להעלות ל‑GitHub ולהשתמש בו כבסיס ל‑CI/CD.

## הפעלה מקומית (ללא Docker)
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS:
source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
# גלישה:
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/health
```

## בדיקות
```bash
pytest -q
```

## Docker – בנייה והרצה
```bash
docker build -t generic-fastapi:local .
docker run -p 8000:8000 generic-fastapi:local
# http://127.0.0.1:8000/
```

## מה הלאה?
1. להעלות את התיקייה ל‑GitHub (או לדחוף בעזרת git).
2. להוסיף workflows ב‑`.github/workflows/` עבור CI ו‑CD (ניצור יחד בהמשך).
