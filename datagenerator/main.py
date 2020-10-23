from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import webServiceStream
from RandomDealData import *
import json
from config import establish_connection


app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return webServiceStream.index()

@app.route('/testservice')
def testservice():
    return webServiceStream.testservice()

@app.route('/streamTest')
def stream():
    return webServiceStream.stream()

@app.route('/streamTest/sse')
def sse_stream():
     return webServiceStream.sse_stream()

@app.route('/login', methods=["POST"])
def login():
    user_request_data = json.loads(request.data.decode('utf-8'))
    username = user_request_data["username"]
    password = user_request_data["password"]
    cnx = establish_connection()
    isLoggedIn = UserDAO.verifyUser(username, password, cnx)
    return jsonify({"isLoggedin": isLoggedIn})

@app.route('/isDbRunning')
def database():
    if establish_connection() != None:
        return jsonify({'isDatabaseUp': True})
    else:
        return jsonify({'isDatabaseUp': False})

def bootapp():
    #global rdd 
    #rdd = RandomDealData()
    #webServiceStream.bootServices()
    app.run(debug=True, port=8080, threaded=True, host=('0.0.0.0'))


if __name__ == "__main__":
      bootapp()
      