import tornado.websocket
import tornado.ioloop
import tornado.web
import tornado.websocket
import anydbm
import json

users = {}	#{username : password}

class WsHandler(tornado.WebSocket.WebSocketHandler):
	self.db = anydbm.open('main_db','n')	

	def open(self):
		if self not in users:
			users.append(self)
			self.write('welcome new user')
		else:
			self.write('welcome back')

	def on_message(self,json_message):
		message = json.loads(json_message)


		if message[0].strip() is 'add':
			
