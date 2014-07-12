import tornado.websocket
import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.httpserver
import anydbm
import json
import os

db = anydbm.open('test_db','n')

class WsHandler(tornado.websocket.WebSocketHandler):

	def open(self):
		self.write_message('Welcome\n')

	def on_message(self,json_message):
		message = json.loads(json_message)

		if message[0].strip() is 'add':
			key = message[1].strip()
			value = message[2].strip()
			db[key] = value

		elif message[0].strip() is 'show':
			dict_str = json.dumps(db)
			self.write_message(dict_str)

		else:
			self.write_message('wrong format!')

	def on_close(self):
		self.send_message('goodbye...')

app = tornado.web.Application([
	(r'/',WsHandler),
])

server = tornado.httpserver.HTTPServer(app)
port = int(os.environ.get("PORT",5000))
server.listen(port)
tornado.ioloop.IOLoop.instance().start()
