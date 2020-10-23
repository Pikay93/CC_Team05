from flask import Flask, Response
from flask_cors import CORS
import webServiceStream
from RandomDealData import *
import DAO

app = Flask(__name__)
CORS(app)

# print(request.data)
    # print(f"username is: {username}, password is: {password}")
    # print(f"Logged in: {isLoggedIn}")
@app.route('/login')
def login():
    user_request_data = json.loads(request.data.decode('utf-8'))
    username = user_request_data["username"]
    password = user_request_data["password"]
    isLoggedIn = DAO.verifyUser("alison","gradprog2016@07")
    return Response(isLoggedIn, status=200, mimetype='application/json')

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


def bootapp():
    #global rdd 
    #rdd = RandomDealData()
    #webServiceStream.bootServices()
    app.run(debug=True, port=8080, threaded=True, host=('0.0.0.0'))


if __name__ == "__main__":
      bootapp()
