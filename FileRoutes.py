from flask import request, jsonify
from flask_restful import Resource
import os

from AuthController import *
from FileController import *

class CreateFile(Resource):
	def __init__(self):
		token = request.headers.get('Authorization')
		self.username = Auth_Controller().verifyToken(token)

	def post(self):
		if not self.username:
			return jsonify(error='invalid token')

		try:
			data = request.get_json(force=True)

			file = File_Controller(self.username)
			result = file.createFile(data['file_path'], data['file_content'])

			if result == 1:
				return jsonify(error='file exists')

			return jsonify(msg='success')

		except Exception as e:
			return jsonify(error=str(e))

class DeleteFile(Resource):
	def __init__(self):
		token = request.headers.get('Authorization')
		self.username = Auth_Controller().verifyToken(token)

	def post(self):
		if not self.username:
			return jsonify(error='invalid token')

		try:
			data = request.get_json(force=True)

			file = File_Controller(self.username)
			result = file.deleteFile(data['file_path'])

			if result == 1:
				return jsonify(error='file does not exist')

			return jsonify(msg='success')
			
		except Exception as e:
			return jsonify(error=str(e))

class OpenFile(Resource):
	def __init__(self):
		token = request.headers.get('Authorization')
		self.username = Auth_Controller().verifyToken(token)

	def post(self):
		if not self.username:
			return jsonify(error='invalid token')

		try:
			data = request.get_json(force=True)

			file = File_Controller(self.username)
			result, content = file.openFile(data['file_path'])

			if result == 1:
				return jsonify(error='file does not exist')

			return jsonify(msg='success', file_content=content)

		except Exception as e:
			return jsonify(error=str(e))

class ListFile(Resource):
	def __init__(self):
		token = request.headers.get('Authorization')
		self.username = Auth_Controller().verifyToken(token)

	def post(self):
		if not self.username:
			return jsonify(error='invalid token')

		try:
			data = request.get_json(force=True)

			file = File_Controller(self.username)
			result, lists = file.listFile(data['folder_path'])

			if result == 1:
				return jsonify(error='directory does not exist')

			return jsonify(msg='success', files=lists)

		except Exception as e:
			return jsonify(error=str(e))

class CreateDir(Resource):
	def __init__(self):
		token = request.headers.get('Authorization')
		self.username = Auth_Controller().verifyToken(token)

	def post(self):
		if not self.username:
			return jsonify(error='invalid token')

		try:
			data = request.get_json(force=True)
			
			file = File_Controller(self.username)
			result = file.createDir(data['folder_path'])

			if result == 1:
				return jsonify(error='directory exists')

			return jsonify(msg='success')

		except Exception as e:
			return jsonify(error=str(e))

class DeleteDir(Resource):
	def __init__(self):
		token = request.headers.get('Authorization')
		self.username = Auth_Controller().verifyToken(token)

	def post(self):
		if not self.username:
			return jsonify(error='invalid token')

		try:
			data = request.get_json(force=True)

			file = File_Controller(self.username)
			result = file.deleteDir(data['folder_path'])

			if result == 1:
				return jsonify(error='directory does not exist')

			return jsonify(msg='success')

		except Exception as e:
			return jsonify(error=str(e))

class ListDir(Resource):
	def __init__(self):
		token = request.headers.get('Authorization')
		self.username = Auth_Controller().verifyToken(token)

	def post(self):
		if not self.username:
			return jsonify(error='invalid token')

		try:
			data = request.get_json(force=True)

			file = File_Controller(self.username)
			result, lists = file.listDir(data['folder_path'])

			if result == 1:
				return jsonify(error='directory does not exist')

			return jsonify(msg='success', dirs=lists)

		except Exception as e:
			return jsonify(error=str(e))

class MoveFile(Resource):
	def __init__(self):
		token = request.headers.get('Authorization')
		self.username = Auth_Controller().verifyToken(token)

	def post(self):
		if not self.username:
			return jsonify(error='invalid token')

		try:
			data = request.get_json(force=True)

			file = File_Controller(self.username)
			result = file.moveFile(data['src'], data['des'])

			if result == 1:
				return jsonify(error='source file does not exist')

			if result == 2:
				return jsonify(error='destination directory does not exist')

			return jsonify(msg='success')

		except Exception as e:
			return jsonify(error=str(e))

class MoveDir(Resource):
	def __init__(self):
		token = request.headers.get('Authorization')
		self.username = Auth_Controller().verifyToken(token)

	def post(self):
		if not self.username:
			return jsonify(error='invalid token')

		try:
			data = request.get_json(force=True)

			file = File_Controller(self.username)
			result = file.moveDir(data['src'], data['des'])

			if result == 1:
				return jsonify(error='source or destination folder does not exist')

			return jsonify(msg='success')

		except Exception as e:
			return jsonify(error=str(e))