from flask import Flask, render_template, Response, request
from flask_sse import sse
from flask_cors import CORS
import requests
import time
import json

app = Flask(__name__)
#app.register_blueprint(sse, url_prefix='/stream')
CORS(app)

@app.route('/deals')
def forwardStream():
    r = requests.get('http://localhost:8080/streamTest', stream=True)
    def eventStream():
            for line in r.iter_lines( chunk_size=1):
                if line:
                    yield 'data:{}\n\n'.format(line.decode())
    return Response(eventStream(), mimetype="text/event-stream")

@app.route('/client/testservice')
def client_to_server():
    r = requests.get('http://localhost:8080/testservice')
    return Response(r.iter_lines(chunk_size=1), mimetype="text/json")

@app.route('/')
@app.route('/index')
def index():
    return "webtier service points are running..."

@app.route('/login',  methods=["POST"])
def login_user():
    print(request.data)
    user_request_data = json.loads(request.data.decode('utf-8'))
    username = user_request_data["username"]
    password = user_request_data["password"]
    
    r = requests.post('http://localhost:8080/login',
                      data=json.dumps({'username': username, "password": password}))
    return Response(r.iter_lines(chunk_size=1), mimetype="text/json")

@app.route('/isDbRunning')
def check_my_database():
    r = requests.get('http://localhost:8080/isDbRunning')
    return Response(r.iter_lines(chunk_size=1), mimetype="text/json")

def get_message():
    """this could be any function that blocks until data is ready"""
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s

def bootapp():
    app.run(port=8090, threaded=True, host=('0.0.0.0'))

if __name__ == '__main__':
     bootapp()
