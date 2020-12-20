import flask
from flask import request, jsonify
import requests
host='0.0.0.0'
port='5000'


app=flask.Flask(__name__)


data = [

{'id': 0,
     'name': 'Adarsh S',
     'age': '24',
     'Education': 'Masters in Cyber Security',
     'year_passout': '2021'},
    {'id': 1,
     'name': 'Aravind',
     'age': '24',
     'Education': 'Masters in Cyber Security',
     'passout': '2021'}



]

@app.route('/', methods=['GET'])
def home_page():
    return '''  <h1> MY GOOGLE CLOUD APP   <h1> '''



@app.route('/gcloudapi/data',methods=['GET'])

def get_api_data():
    return jsonify(data)




app.run(host, port)
