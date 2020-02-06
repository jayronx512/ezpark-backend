from flask import Blueprint, request, json, jsonify
from models.user import User


users_api_blueprint = Blueprint('users_api',
                             __name__,
                             template_folder='templates')

@users_api_blueprint.route('/', methods=['GET'])
def index():
    return "USERS API"

@users_api_blueprint.route('/signup', methods=['POST'])
def create():
    username = request.json.get('username')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    email = request.json.get('email')
    password = request.json.get('password')
    hp_number = request.json.get('hp_number')

    user = User(username=username, email=email, first_name = first_name, last_name = last_name, password=password, hp_number=hp_number)

    if user.save():
        # access_token
        responseObj = {
            'status': 'success',
            'message': 'User successfully created',
            'user': {"id": int(user.id), "username": user.username, "email": user.email, "first_name": user.first_name, "last_name": user.last_name, "hp_number": user.hp_number}
        }

        return jsonify(responseObj), 200

    else: 
        responseObj = {
            'status': 'failed',
            'message': user.errors
        }

        return jsonify(responseObj), 400
    
