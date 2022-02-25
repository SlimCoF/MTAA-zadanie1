import sipfullproxy as s
import socket
import logging
import sys
import socketserver
import time

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='proxy.log', level=logging.INFO,
                        datefmt='%H:%M:%S')
    logging.info(time.strftime("%a, %d %b %Y %H:%M:%S ", time.localtime()))
    hostname = socket.gethostname()
    logging.info(hostname)
    ipaddress = socket.gethostbyname(hostname)
    if ipaddress == "127.0.0.1":
        ipaddress = sys.argv[1]
    logging.info(ipaddress)
    s.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress, s.PORT)
    s.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress, s.PORT)
    server = socketserver.UDPServer((s.HOST, s.PORT), s.UDPHandler)
    print("Server: " + str(ipaddress) + " is running on port: " + str(s.PORT))
    server.serve_forever()
