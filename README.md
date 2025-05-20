# Flask To-Do API

## Setup

1. Skapa och aktivera ett virtuellt miljö:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. Installera paket:
   ```bash
   pip install -r requirements.txt
   ```

3. Starta server:
   ```bash
   python app.py
   ```

## .env Exempel

```
DATABASE_URL=sqlite:///todos.db
PORT=5000
```