import os
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get("APP_SECRET_KEY")
jwt = JWTManager(app)

MAIN_VERSION = 'v1'


@app.route(f'/api/{MAIN_VERSION}/auth', methods=['POST'])
def auth():
    username = request.json.get('username')
    password = request.json.get('password')

    if username == 'admin' and password == 'password':
        access_token = create_access_token(identity=username)

        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'error': 'Credenciais inválidas'}), 401


@app.route(f'/api/{MAIN_VERSION}/number', methods=['GET', 'POST'])
@jwt_required()
def get_random_number():
    import random
    number = random.randint(1, 1000)
    return jsonify({'number': number}), 200


@app.route("/")
def home():
    return jsonify({'msg': 'hooooome'})


@app.route('/<path:any_path>',  methods=['GET', 'POST'])
def any_route(any_path):
    return jsonify({'msg': f'O caminho fornecido foi: {any_path}'})


if __name__ == '__main__':
    app.run()
