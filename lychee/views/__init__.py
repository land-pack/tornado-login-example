from __future__ import absolute_import

import tornado

class BaseHandler(tornado.web.RequestHandler):
	
	def get_current_user(self):
		return self.get_secure_cookie("user")
