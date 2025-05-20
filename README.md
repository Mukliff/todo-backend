# To-Do Backend (Flask API)

Detta är backend-delen av en To-Do-applikation byggd med Flask och SQLite. Den erbjuder ett RESTful API för att hantera uppgifter (To-Dos) med stöd för GET, POST, PUT och DELETE.

## ✅ Funktionalitet

- Hämta alla To-Dos eller en specifik
- Skapa en ny To-Do
- Uppdatera en To-Do
- Radera en To-Do
- Felhantering (404, 400)

## 📦 Installation

```bash
cd backend
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🚀 Starta servern

```bash
flask run
```

Servern körs som standard på `http://localhost:5000`.

## 🗃️ Databas

- **Databas:** SQLite
- En lokal fil `todos.db` skapas automatiskt.

## 🔐 Miljövariabler

Skapa en `.env`-fil i `backend/`-mappen:

```env
FLASK_APP=app.py
FLASK_ENV=development
DATABASE_URL=sqlite:///todos.db
PORT=5000
```

## 📁 Projektstruktur

```
backend/
├── app.py
├── controllers/
│   └── todo_controller.py
├── routes/
│   └── todo_routes.py
├── models/
│   └── todo_model.py
├── .env
└── requirements.txt
```

## 📝 Övrigt

- Alla endpoints finns dokumenterade i `routes/todo_routes.py`
- Felhantering implementeras i `controllers/todo_controller.py`
