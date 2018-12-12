import pickledb
import uuid

class Users_Model(object):
	def __init__(self):
		self.db = pickledb.load('users.db', True)

		try:
			self.list()
		except KeyError:
			self.db.dcreate('userdb')

	def add(self, username, password):
		id = uuid.uuid1()
		data = { 'username': username, 'password': password }

		self.db.dadd('userdb', ("{}".format(str(id)), data))

	def list(self):
		return self.db.dgetall('userdb')

	def get(self, id):
		return self.db.dget('userdb', id)

	def find(self, username):
		for x in self.list():
			data = self.get(x)
			if (data['username'] == username):
				return data	

		return None

	def empty(self):
		try:
			self.db.drem('userdb')
			self.db.dcreate('userdb')
		except KeyError:
			self.db.dcreate('userdb')

	def remove(self, id):
		self.db.dpop('userdb', id)