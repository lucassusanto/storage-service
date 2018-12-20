import pickledb
import uuid

class Users_Model(object):
	def __init__(self):
		self.db = pickledb.load('db/users.db', True)

		try:
			self.list()
		except KeyError:
			self.db.dcreate('userdb')

	def list(self):
		return self.db.dgetall('userdb')

	def get(self, id):
		return self.db.dget('userdb', id)

	# Create Entry
	def add(self, username, password, usedSpace):
		id = uuid.uuid1()
		data = { 'username': username, 'password': password, 'used_space': usedSpace, 'free_space': 1024**3 }

		self.db.dadd('userdb', ("{}".format(str(id)), data))

	# Getting Data
	def find(self, username):
		for x in self.list():
			data = self.get(x)
			if (data['username'] == username):
				return data	

		return None

	# High Level Controller
	def createUser(self, username, password):
		self.add(username, password, 0);

	def updateUsedSpace(self, username, size):
		for x in self.list():
			data = self.get(x)
			if (data['username'] == username):
				self.add(username, data['password'], data['used_space'] + size)
				self.remove(x)
				return True

		return False

	def canAddFile(self, username, size):
		for x in self.list():
			data = self.get(x)
			if (data['username'] == username):
				if(data['used_space'] + size > data['free_space']):
					return False
				return True

		return False

	# Purging
	def remove(self, id):
		self.db.dpop('userdb', id)

	def empty(self):
		try:
			self.db.drem('userdb')
			self.db.dcreate('userdb')
		except KeyError:
			self.db.dcreate('userdb')