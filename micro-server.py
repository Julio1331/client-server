#!/usr/bin/env python3
# A web server to echo back a request's headers and data.
#
# Usage: ./webserver
#        ./webserver 0.0.0.0:5000

from http.server import HTTPServer, BaseHTTPRequestHandler
#from sys import argv
from urllib.parse import parse_qs
from urllib.parse import urlparse
import serialcom

#importar modulo de envio de datos
import serialcom


BIND_HOST = 'localhost'
PORT = 6777

global vectora
global vectorn

vectorn = ""
vectora = ""

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print ("por fuera get: ", vectorn)
        self.write_response(b'')

    def do_POST(self): #no usado
        #print ("por fuera post: ", vectorn)
        content_length = int(self.headers.get('content-length', 0))
        #content_length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(content_length)
        self.write_response(body)

    # def do_OPTIONS(self): #no usado
    #     content_length = int(self.headers.get('content-length', 0))
    #     print(content_length)
    #     #content_length = int(self.headers.get('content-length', 0))
    #     body = self.rfile.read(content_length)
    #     print("Cuerpo:")
    #     print(body)
    #     print("Fin Cuerpo \n")

    #    self.write_response(body)

    #def write_response(self, content,vectorn,vectora):
    def write_response(self, content):
        self.send_response(418)
        self.end_headers()
        self.wfile.write(content)
        print("recepción: ",content)

        # print(type(content))
        vectorn = content.decode('utf-8') # convierto a utf-8
        #transmision del vector recibido
        serialcom.transmision(vectorn)
        print('\n\n')
        #vectora = vectorn

        #estado = self.request.get('estado') # this will get the value from the field named username
        #self.response.write(name) # this will write on the document

        #print(self.headers)
        
        #foca = self.requestline
        #estopa = self.path
        #print(estopa)
        #parsed_path = urlparse(self.path)
        # print(parsed_url.params)
        # print(parsed_url.path)
        # print(parsed_url.encode)

        #query = parsed_path.query
        #captured_values = parse_qs(query)
        
        #print(captured_values)
        #print("The type is : ", type(captured_values))
        #data = content.decode('utf-8');
        #print(data)
        #print(name)
    
# if len(argv) > 1:
#     arg = argv[1].split(':')
#     BIND_HOST = arg[0]
#     PORT = int(arg[1])

print(f'Listening on http://{BIND_HOST}:{PORT}\n')
httpd = HTTPServer((BIND_HOST, PORT), SimpleHTTPRequestHandler)
httpd.serve_forever()

# vectorn = [0, 0, 0, 0]
# vectora = [0, 0, 0, 1]
# serialcom.transmision(vectorn, vectora)