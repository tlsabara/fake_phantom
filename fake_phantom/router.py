from views import request_recived_repot
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask import jsonify
# def route_get_urls(url_path: str) -> any:
#     if str(url_path) == "/repport":
#         return request_recived_repot()
#     return False

def auth(request):
    username = request.json.get('username')
    password = request.json.get('password')

    if username == 'admin' and password == 'password':
        access_token = create_access_token(identity=username)

        return jsonify({'access_token': access_token}), 200
    else:
        return jsonify({'error': 'Credenciais inválidas'}), 401


def home():
    return jsonify({'msg': 'Seu fake phantom esta ONLINE'})


def whitelabel(**kwargs):
    url_path = kwargs.get('any_path')
    request = kwargs.get('req')
    return jsonify(
        {
            'msg': f'O caminho fornecido foi: {url_path}',
            'body': str(request.data)
        }
    )