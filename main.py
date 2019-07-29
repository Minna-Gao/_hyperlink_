import os
import #our own datastore py
import webapp2
import datetime
from google.appengine.api import users
from google.appengine.ext.webapp import template


def render_template(handler, file_name, template_values):
    path = os.path.join(os.path.dirname(__file__), 'templates/', file_name)
    handler.response.out.write(template.render(path, template_values))


class MainHandler(webapp2.RequestHandler):
    def get(self):
    render_template(self, 'mainpage.html', values)



app = webapp2.WSGIApplication([
    ('.*', MainHandler),
])