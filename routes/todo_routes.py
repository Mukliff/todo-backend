from flask import Blueprint
from controllers import todo_controller

todo_bp = Blueprint('todos', __name__)

todo_bp.route('/', methods=['GET'])(todo_controller.get_all_todos)
todo_bp.route('/<int:todo_id>', methods=['GET'])(todo_controller.get_todo)
todo_bp.route('/', methods=['POST'])(todo_controller.create_todo)
todo_bp.route('/<int:todo_id>', methods=['PUT'])(todo_controller.update_todo)
todo_bp.route('/<int:todo_id>', methods=['DELETE'])(todo_controller.delete_todo)