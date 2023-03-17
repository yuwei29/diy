'''
The MIT License (MIT)
Copyright (c) 2013 Dave P.
'''
from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler

if __name__ == "__main__":
    # openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem
    httpd = HTTPServer(('', 8080), SimpleHTTPRequestHandler)
    # httpd.socket = ssl.wrap_socket(httpd.socket, server_side=True, certfile='./cert.pem', 
    #                              keyfile='./key.pem', ssl_version=ssl.PROTOCOL_TLSv1)
    httpd.serve_forever()