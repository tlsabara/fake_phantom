import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from pathlib import Path
import os
from dotenv import load_dotenv
from datetime import datetime
from orm.queries import initialize_data, insert_request_data, collect_response_data
from router import route_get_urls

ROOT_DIR = Path(os.path.abspath(os.path.curdir))
load_dotenv()


class APIServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f'{"requisicao":-^50}')
        print('ENDPOINT -->> ', self.path)
        timestamp_ = datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
        print("GET hora: ", timestamp_)
        print(self.headers.as_string())

        msg_get_response = route_get_urls(self.path)

        if msg_get_response is False:
            content_type = 'application/json'
            clean_response = 'GET respondido'
            msg_get_response = collect_response_data(where_tag="def_GET_200")
            msg_get_response = msg_get_response if msg_get_response else clean_response
            msg_get_response = bytes(msg_get_response, 'utf-8')
        else:
            content_type = 'text/html'

        self.send_response(200)
        self.send_header('Content-type', content_type)
        self.end_headers()

        self.wfile.write(msg_get_response)
        print(f'{" fim requisicao ":-^50}')

    def do_POST(self):
        print(f'{" requisicao ":-^50}')
        print('ENDPOINT -->> ', self.path)
        timestamp_ = datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
        print("POST hora: ", timestamp_)
        print(self.headers.as_string())
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        clean_response = 'POST respondido'
        length = int(self.headers["Content-Length"])

        insert_request_data(self.path, self.rfile.read(length).decode('UTF-8'))
        msg_get_response = collect_response_data(where_tag="def_POST_200")
        msg_get_response = msg_get_response if msg_get_response else clean_response
        self.wfile.write(bytes(msg_get_response, 'utf-8'))
        print(f'{" fim requisicao ":-^50}')

    def do_PUT(self):
        print(f'{" requisicao ":-^50}')
        print('ENDPOINT -->> ', self.path)
        timestamp_ = datetime.now().strftime('%Y_%m_%d__%H_%M_%S')
        print(self.headers)
        print("PUT hora: ", timestamp_)
        print(self.headers.as_string())
        length = int(self.headers["Content-Length"])
        clean_response = 'PUT respondido'
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        insert_request_data(self.path, str(self.rfile.read(length)))
        msg_get_response = collect_response_data(where_tag="def_PUT_200")
        msg_get_response = msg_get_response if msg_get_response else clean_response
        self.wfile.write(bytes(msg_get_response, 'utf-8'))
        print(f'{" fim requisicao ":-^50}')


if __name__ == '__main__':
    print('Iniciando ENDPOINT')
    FILE_LOG = ROOT_DIR / 'app_logs' / f'run_{datetime.now().strftime("%Y%m%d%H%M%S")}'
    FILE_LOG.mkdir(parents=True, exist_ok=True)
    FILE_LOG = FILE_LOG
    print('Carregando DB')

    if not initialize_data():
        print("DB ERROR")
    else:
        base_port = 8000
        with HTTPServer(('', base_port), APIServer) as local_api_server:
            print(f'Server ON, listen: {base_port}\n{"-" * 50}')
            local_api_server.serve_forever()
