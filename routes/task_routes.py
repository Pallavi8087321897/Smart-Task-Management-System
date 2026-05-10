from analytics.analytics import task_analytics
from flask import Blueprint, request, jsonify
from models.task import Task
from extensions import db, socketio

task_bp = Blueprint('task', __name__)

# ADD TASK API
@task_bp.route('/tasks', methods=['POST'])
def add_task():

    data = request.json

    task = Task(
        title=data['title'],
        description=data['description'],
        priority=data['priority'],
        status=data['status']
    )

    db.session.add(task)
    db.session.commit()

    # WebSocket Notification
    socketio.emit('task_update', {
        "message": "New task added"
    })

    return jsonify({
        "message": "Task added successfully"
    })


# GET ALL TASKS API
@task_bp.route('/tasks', methods=['GET'])
def get_tasks():

    tasks = Task.query.all()

    output = []

    for t in tasks:

        output.append({
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "priority": t.priority,
            "status": t.status,
            "created_date": t.created_date
        })

    return jsonify(output)


# UPDATE TASK API
@task_bp.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):

    task = Task.query.get(id)

    if not task:
        return jsonify({
            "message": "Task not found"
        })

    data = request.json

    task.title = data['title']
    task.description = data['description']
    task.priority = data['priority']
    task.status = data['status']

    db.session.commit()

    return jsonify({
        "message": "Task updated successfully"
    })


# DELETE TASK API
@task_bp.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):

    task = Task.query.get(id)

    if not task:
        return jsonify({
            "message": "Task not found"
        })

    db.session.delete(task)
    db.session.commit()

    return jsonify({
        "message": "Task deleted successfully"
    })

# ANALYTICS API
@task_bp.route('/analytics', methods=['GET'])
def analytics():

    result = task_analytics()

    return jsonify(result)