from flask import Blueprint, request, jsonify
from models.user import User
from extensions import db

auth_bp = Blueprint('auth', __name__)

# REGISTER API
@auth_bp.route('/register', methods=['POST'])
def register():

    data = request.json

    user = User(
        username=data['username'],
        password=data['password']
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    })


# LOGIN API
@auth_bp.route('/login', methods=['POST'])
def login():

    data = request.json

    user = User.query.filter_by(
        username=data['username'],
        password=data['password']
    ).first()

    if user:
        return jsonify({
            "message": "Login successful"
        })

    return jsonify({
        "message": "Invalid username or password"
    })