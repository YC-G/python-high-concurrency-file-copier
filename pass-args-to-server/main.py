import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
from tornado.options import options, define
from tornado.web import RequestHandler

define("port", default=8000, type=int, help="Run server on the given port.")

class IndexHandler(RequestHandler):
    def get(self):
        # Pass arguments to the server from the header or the body
        # http://127.0.0.1:8000/?subject=python&subject=cpp
        # Postman: body, x-www-form-urlencoded
        # subjects = self.get_query_arguments("subject")
        # subjects = self.get_body_arguments("subject")
        # subjects = self.get_arguments("subject")
        # self.write(str(subjects))
        # Pass arguments to the server as JSON type
        # self.request.headers.get("Content-Type").startwith("application/json")
        # json_data = self.request.body
        # json_args = json.loads(json_data)
        # self.write(ison_args)
        # Write a hyperlink
        # self.write('<a href="' + self.reverse_url("cpp_url") + '">cpp</a>')
        self.write("Hello itcast.")

class SubjectCityHandler(RequestHandler):
    def get(self, subject, city):
        self.write(("Subject: %s<br/>City: %s" % (subject, city)))

class SubjectDateHandler(RequestHandler):
    def get(self, date, subject):
        self.write(("Date: %s<br/>Subject: %s" % (date, subject)))

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/", IndexHandler),
        # no name
        (r"/sub-city/(.+)/([a-z]+)", SubjectCityHandler),
        # with name
        (r"/sub-date/(?P<subject>.+)/(?P<date>\d+)", SubjectDateHandler),
    ])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


