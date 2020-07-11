from flask import Flask,jsonify
from flask_restful import Resource,Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return jsonify({"message" : "successfully Done deploying"})

@app.route('/home')
def home_1():
    return jsonify({"message" : "successfully Done deploying"})

app.run(debug=True)