from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from routes.todo_routes import todo_bp
import os

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models.todo import Todo
with app.app_context():
    db.create_all()

app.register_blueprint(todo_bp, url_prefix='/api/todos')

if __name__ == '__main__':
    app.run(port=int(os.getenv("PORT", 5000)), debug=True)