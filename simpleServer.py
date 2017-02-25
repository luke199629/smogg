# -*- coding: utf-8 -*-
# @Author: luke199629
# @Date:   2017-02-25 03:51:46
# @Last Modified by:   luke199629
# @Last Modified time: 2017-02-25 03:51:50
import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()