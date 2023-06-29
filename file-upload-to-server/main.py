import tornado.web
import tornado.ioloop
import tornado.httpserver

import tornado.options

from tornado.web import RequestHandler, url
from tornado.options import define, options

tornado.options.define("port", type=int, default=8000, help="server port")

class IndexHandler(RequestHandler):
    def get(self):
        self.write("Hello itcast.")

class uploadHandler(RequestHandler):
    def post(self):
        files = self.request.files
        img_files = files["img"]
        if img_files:
            img_file = img_files[0]["body"]
            # w+: both write and read
            # wb: write as binary mode, \n -> \r\n in Windows
            # r+: both read and write
            # rb: read as binary mode, \r\n -> \n in Windows
            file = open("./itcast", "w+")
            file.write(img_file)
            file.close()
        self.write("OK")

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [(r"/", IndexHandler),
        (r"/upload", uploadHandler),
        ],)
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()