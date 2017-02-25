# -*- coding: utf-8 -*-
# @Author: luke199629
# @Date:   2017-02-25 03:51:46
# @Last Modified by:   luke199629
# @Last Modified time: 2017-02-25 04:03:48
import time
import SimpleHTTPServer
import SocketServer

PORT = 8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass
httpd.server_close()
print time.asctime(), "Server Stops"