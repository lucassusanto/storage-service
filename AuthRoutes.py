from flask import request, jsonify
from flask_restful import Resource

from AuthController import *

class Login(Resource):
	def post(self):
		try:
			data = request.get_json(True)

			username = data['username']
			password = data['password']
			
			auth = Auth_Controller()
			result = auth.login(username, password)

			if result is None:
				return jsonify(error='invalid username or password')

			return jsonify(msg='success', token=result)

		except Exception as e:
			return jsonify(error=str(e))

class Register(Resource):
	def post(self):
		try:
			data = request.get_json(True)

			username = data['username']
			password = data['password']
			
			auth = Auth_Controller()
			result = auth.register(username, password)
			
			if result is None:
				return jsonify(error='user has already been registered!')

			return jsonify(msg='success')
			
		except Exception as e:
			return jsonify(error=str(e))

class AccountStatus(Resource):
	def __init__(self):
		token = request.headers.get('Authorization')
		self.username = Auth_Controller().verifyToken(token)

	def get(self):
		if not self.username:
			return jsonify(error='invalid token')

		try:
			result, usedSpace, freeSpace = Auth_Controller().cekStatus(self.username)
			if result == 1:
				return jsonify(error='User not found')

			return jsonify(msg='success', used_space=usedSpace, free_space=freeSpace, available_space=(freeSpace - usedSpace))

		except Exception as e:
			return jsonify(error=str(e))