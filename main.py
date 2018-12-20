from flask import Flask,request,jsonify
from flask_restful import Resource, Api, reqparse
from gevent.pywsgi import WSGIServer
import os

# Controllers

from AuthRoutes import *
from FileRoutes import *

class Version(Resource):
	def get(self):
		iplist = os.popen("ifconfig eth0 | grep 'inet addr'").readlines()
		my_ip = "".join(iplist)
		return { 'info' : '0.01', 'ip' : "{}" . format(my_ip) }

# Bootstrap

if not os.path.isdir('storage'):
	os.mkdir('storage')
if not os.path.isdir('db'):
    os.mkdir('db')

if os.path.isfile('db/users.db') and os.path.getsize('db/users.db') == 0:
	os.remove('db/users.db')

# Application

app = Flask(__name__)
api = Api(app)

# Routes

api.add_resource(Login, '/login')
api.add_resource(Register, '/register')
api.add_resource(AccountStatus, '/status')
api.add_resource(Version, '/version')

api.add_resource(CreateFile, '/create')
api.add_resource(DeleteFile, '/delete')
api.add_resource(OpenFile, '/open')
api.add_resource(ListFile, '/lsfile')
api.add_resource(CreateDir, '/mkdir')
api.add_resource(DeleteDir, '/rmdir')
api.add_resource(ListDir, '/lsdir')
api.add_resource(MoveFile, '/mvfile')
api.add_resource(MoveDir, '/mvdir')

# Start Service

http_server = WSGIServer(('', 5000), app)
http_server.serve_forever()
