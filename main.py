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
		#self.write_message(str(message))

		if message[0][0].strip() == 'add':
			try:
				db[message[0][1]] = message[0][2]
				self.write_message('success')
			except Exception,e:
				self.write_message('error is here ' + str(e))

		elif message[0].strip() == 'show':
			try:
				dict_str = json.dumps(db)
				self.write_message(dict_str)
			except Exception,e:
				self.write_message(str(e))

		else:
			self.write_message('wrong format!')

	def on_close(self):
		self.write_message('goodbye...')

app = tornado.web.Application([
	(r'/',WsHandler),
])

server = tornado.httpserver.HTTPServer(app)
port = int(os.environ.get("PORT",5000))
server.listen(port)
tornado.ioloop.IOLoop.instance().start()
