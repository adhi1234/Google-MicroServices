import requests
import pprint
import flask
from flask import request, jsonify
host='0.0.0.0'
port='8888'

details=requests.get('http://localhost:4444/gcloudapi/data')
print("GETTING DATA FROM GCLOUD APP")
pprint.pprint(details.json())


master_app=flask.Flask(__name__)


data_2 = [

{'id': 2,
     'name': 'Elwin ',
     'age': '24',
     'Education': 'Masters in Cyber Security',
     'year_passout': '2021'},
    {'id': 3,
     'name': 'Megha',
     'age': '24',
     'Education': 'Masters in Cyber Security',
     'passout': '2021'}

]


@master_app.route('/', methods=['GET'])
def home_page():
    return '''  <h1> Welcome  to Master App - Gcloud<h1> '''



@master_app.route('/data',methods=['GET'])

def get_api_data():
    return ''' <h1>Hello world</h1>'''

@master_app.route('/masterapp/data',methods=['GET'])

def get_masterapi_data():
    return jsonify(details.json())


master_app.run(host,port)
