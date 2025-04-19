import SimpleHTTPServer
import SocketServer
import socket
import webbrowser
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname_ex(hostname)[2][1]
print(ip)
PORT = 8000  

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer((ip, PORT), Handler)

print("Web server started: http://%s:%s" % (ip, PORT))
webbrowser.open_new("http://%s:%s" % (ip, PORT))

httpd.serve_forever()

