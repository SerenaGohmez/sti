#!flask/bin/python
from flask import Flask,jsonify,request,abort
import requests

app = Flask(__name__)

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
		"Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0OTc2Nzg2NzcsImV4cCI6MTQ5Nzc2NTA3N30.OXDDuxmDCUUOtgxrIV0CGRJ0YMXkIcONXxQNL3IdAvk"
	}

        response = requests.post(url, headers=headers, data=payload, verify=False)
        return payload

@app.route('/users/read', methods=['GET'])
def get_users():
	
	url = "https://localhost:8443/api/2.0/users"	

	headers = {
                "Content-Type": "application/json",
		"Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0OTc2Nzg2NzcsImV4cCI6MTQ5Nzc2NTA3N30.OXDDuxmDCUUOtgxrIV0CGRJ0YMXkIcONXxQNL3IdAvk"
	}
	
	response = requests.get(url, headers=headers, verify=False)
	return response.text

@app.route('rackHD/users/update', methods=['DELETE','POST'])
def update_users():

        username = request.json['username']
        url = "https://localhost:8443/api/2.0/users" + "/" + username

        headers = {
                "Content-Type": "application/json",
                "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0OTc2Nzg2NzcsImV4cCI6MTQ5Nzc2NTA3N30.OXDDuxmDCUUOtgxrIV0CGRJ0YMXkIcONXxQNL3IdAvk"
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
                "Authorization": "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyIjoiYWRtaW4iLCJpYXQiOjE0OTc2Nzg2NzcsImV4cCI6MTQ5Nzc2NTA3N30.OXDDuxmDCUUOtgxrIV0CGRJ0YMXkIcONXxQNL3IdAvk"
        }

        response = requests.delete(url, headers=headers, verify=False)
        return response.text

if __name__ == '__main__':
        app.run(debug=True)
