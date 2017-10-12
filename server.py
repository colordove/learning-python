from wsgiref.simple_server import make_server
from hello_name import application

httpServer = make_server('', 4600, application)
print('Server is running at port 4600')
httpServer.serve_forever()