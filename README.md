# STI SERENA'S ACCOUNTS CRUD 

RackHD Accounts appcrud.py Version 1.0 20/06/2017

USAGE NOTES
------------

- Change directory to the todo-api by typing cd todo-api

- Run the program in RackHD using ./appcrud.py

- Get a authentication token first.

- "content-type: application/json" must be included in header whenever sending json data.

- Pipe output to python -m json.tool to view the data in a better format.(e.g. curl -X GET | python -m json.tool)


LOGIN
------

- Login to obtain auth_token to carry out CRUD operation on RackHD.

- Administrator Credentials: 
admin:admin123

- Get a authentication token first by typing:

- CURL Command: 
curl http://localhost:5000/users/login -X POST -H "Content-Type:application/json" -d '{"username":"admin", "password":"admin123", "role": "Administrator" }'


===============================================

CREATE ACCOUNT
--------------

- CURL Command: 
curl http://localhost:5000/users/create -H "Content-Type: application/json" -X POST -d '{"username":"<username>", "password":"<password>", "role":"<role>"}'


READ ACCOUNT(S)
---------------

- CURL Command: 
curl http://localhost:5000/users/read | python -m json.tool


UPDATE ACCOUNT
--------------

- CURL Command:
curl http://localhost:5000/users/update -X DELETE -H "Content-Type:application/json" -d '{"username":"<username>", "password":"<password>", "role": "<role>" }'


DELETE ACCOUNT
--------------

- CURL Command:
curl -i http://localhost:5000/users/delete -X DELETE -H "Content-Type:application/json" -d '{"username":"<username>"}'
