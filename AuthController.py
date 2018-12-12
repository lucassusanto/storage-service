import bcrypt
import datetime
import jwt
import os

from UsersModel import *

class Auth_Controller(object):
	def login(self, username, password):
		user_detail = Users_Model().find(username)

		if user_detail is None:
			return None

		hashed = user_detail['password']
		
		if not bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8')):
			return None

		token_expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)

		token_body = dict()
		token_body['username'] = username
		token_body['exp'] = token_expiration
		
		return Token_Model(token_body).getEncoded()

	def register(self, username, password):
		user = Users_Model()
		if user.find(username):
			return None

		hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
		user.add(username, hashed)

		os.mkdir('storage\\' + username)

		return True
		
	def verifyToken(self, data):
		try:
			result = Token_Model(data.encode('utf-8')).getDecoded()
			return result['username']
		except:
			return None

class Token_Model(object):
	def __init__(self, data={}):
		self.key = 'kaoskakibiru12345'
		self.data = data

	def getEncoded(self):
		return jwt.encode(self.data, self.key, 'HS256')

	def getDecoded(self):
		return jwt.decode(self.data, self.key, 'HS256')