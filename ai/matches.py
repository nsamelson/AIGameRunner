import cherrypy
import sys
import pickle
import socket
import json
import time

s= 0


def create_socket():
    global s
    address = ("localhost", 8181)
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(address)
    # s.listen(1)
    # conn, addr = s.accept()
    
    
    
def data_sending():
    
    create_socket()
    # s.connect(("127.0.0.1",8181))
    data = "heyy".encode()
    sent =s.send(data)
    if sent == len(data):
        print("sending complete")
    
def data_receiving():
    data_sending()
    received = s.recv(4096).decode ()
    time.sleep(2)
    print("received", received )
    s.close()
    # return received
class Server:
    
    @cherrypy.tools.json_in()
    
        
    @cherrypy.expose
    def default(self,atr= "abc"):
        return "<h1 >404 </h1 ><p> Page not found ! Fin du monde !</p>"

    @cherrypy.expose
    def move(self):
        # Deal with CORS
        cherrypy.response.headers['Access-Control-Allow-Origin'] = '*'
        cherrypy.response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        cherrypy.response.headers['Access-Control-Allow-Headers'] = 'Content-Type, Authorization, X-Requested-With'
        if cherrypy.request.method == "OPTIONS":
            return ''
        
        body = cherrypy.request.json

        # code ici de l'ia


        print(body)
        return "{""move"": 1}"

    @cherrypy.expose
    def ping(self):
        
        return "pong"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        port=int(sys.argv[1])
    else:
        port=8080

    data_receiving()
    
    # cherrypy.config.update({'server.socket_host': '0.0.0.0', 'server.socket_port': port})
    # cherrypy.quickstart(Server())

    