#!flask/bin/python
from flask import Flask,jsonify,request,abort,make_response,url_for
import requests, json

from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)

@auth.get_password
def get_password(username):
	if username == 'admin':
		return 'hi'
	return None

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error': 'Unauthorized Access'}), 401)

@app.errorhandler(400)
def bad_request(error):
	return make_response(jsonify({'error':'Bad Request'}), 400)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error':'Not Found'}), 404)

@app.errorhandler(405)
def method_not_allowed(error):
	return make_response(jsonify({'error':'Method Not Allowed'}), 405)

@app.route('/')
@auth.login_required
def index():
	return "Hello, %s!" % auth.username()

@app.route('/users/login', methods=['POST'])
def users_login():
	if not request.json or not 'username' in request.json:
        	abort(400)

	username = request.json['username']
        password = request.json['password']

        url = "https://localhost:8443/login"

        payload = '{"username" : "' + username + '", "password" : "' + password +'"}'

        headers = {
                "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, data=payload, verify=False)
        return response.text


@app.route('/users/create', methods=['POST'])
def create_users():

        username = request.json['username']
      	password = request.json['password']
	role = request.json['role']	
	url = "https://localhost:8443/api/2.0/users"

	payload = '{"username":"%s","password":"%s","role":"%s"}' % (username,password,role)

	headers = {
                "Content-Type": "application/json",
		"Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0OTc5NDM2MTksImV4cCI6MTQ5ODAzMDAxOX0.NzjGL4hgvchyvQw3ORQ4AQiTlcmRKmnLz4oz-SBCLJI"
	}

        response = requests.post(url, headers=headers, data=payload, verify=False)
        return payload

@app.route('/users/read', methods=['GET'])
def get_users():
	
	url = "https://localhost:8443/api/2.0/users"	

	headers = {
                "Content-Type": "application/json",
		"Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0OTc5NDM2MTksImV4cCI6MTQ5ODAzMDAxOX0.NzjGL4hgvchyvQw3ORQ4AQiTlcmRKmnLz4oz-SBCLJI"
	}
	
	response = requests.get(url, headers=headers, verify=False)
	return response.text

@app.route('/users/update', methods=['DELETE','POST'])
def update_users():

        username = request.json['username']
        url = "https://localhost:8443/api/2.0/users" + "/" + username

        headers = {
                "Content-Type": "application/json",
                "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0OTc5NDM2MTksImV4cCI6MTQ5ODAzMDAxOX0.NzjGL4hgvchyvQw3ORQ4AQiTlcmRKmnLz4oz-SBCLJI"
        }

        responsedel = requests.delete(url, headers=headers, verify=False)
        
        username = request.json['username']
        password = request.json['password']
        role = request.json['role']
        url = "https://localhost:8443/api/2.0/users"

        payload = '{"username":"%s","password":"%s","role":"%s"}' % (username,password,role)

	response = requests.post(url, headers=headers, data=payload, verify=False)

	return response.text


@app.route('/users/delete', methods=['DELETE'])
def del_users():
  
	username = request.json['username']
	url = "https://localhost:8443/api/2.0/users" + "/" + username

        headers = {
                "Content-Type": "application/json",
                "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0OTc5NDM2MTksImV4cCI6MTQ5ODAzMDAxOX0.NzjGL4hgvchyvQw3ORQ4AQiTlcmRKmnLz4oz-SBCLJI"
        }

        response = requests.delete(url, headers=headers, verify=False)
        return response.text

if __name__ == '__main__':
        app.run(debug=True)
