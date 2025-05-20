from flask import request, jsonify
from models.todo import Todo
from app import db

def get_all_todos():
    todos = Todo.query.all()
    return jsonify([{'id': t.id, 'title': t.title, 'completed': t.completed} for t in todos])

def get_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    return jsonify({'id': todo.id, 'title': todo.title, 'completed': todo.completed})

def create_todo():
    data = request.get_json()
    if not data or not data.get('title'):
        return jsonify({'error': 'Invalid data'}), 400
    new_todo = Todo(title=data['title'], completed=False)
    db.session.add(new_todo)
    db.session.commit()
    return jsonify({'id': new_todo.id, 'title': new_todo.title, 'completed': new_todo.completed}), 201

def update_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    data = request.get_json()
    todo.title = data.get('title', todo.title)
    todo.completed = data.get('completed', todo.completed)
    db.session.commit()
    return jsonify({'id': todo.id, 'title': todo.title, 'completed': todo.completed})

def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({'error': 'Todo not found'}), 404
    db.session.delete(todo)
    db.session.commit()
    return jsonify({'message': 'Todo deleted'})