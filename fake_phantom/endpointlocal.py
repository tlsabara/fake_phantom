import os
import random
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from dotenv import load_dotenv
import fake_phantom.router as router

load_dotenv()
app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = os.environ.get("APP_SECRET_KEY")
jwt = JWTManager(app)

MAIN_VERSION = 'v1'


@app.route(f'/api/{MAIN_VERSION}/auth', methods=['POST'])
def auth_route():
    return router.auth(request)


@app.route(f'/api/{MAIN_VERSION}/number', methods=['GET', 'POST'])
@jwt_required()
def get_random_number():
    number = random.randint(1, 1000)
    return jsonify({'number': number}), 200


@app.route("/")
def home_route():
    return router.home()


@app.route('/<path:any_path>',  methods=['GET', 'POST'])
def any_route(any_path):
    return router.whitelabel(
        any_path=any_path,
        req=request
    )

if __name__ == '__main__':
    app.run()
