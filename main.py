import sipfullproxy as sip
import socketserver as ss
import logging as log
import time as t
import socket
import sys

def runSIP():
    log.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', filename='call_log.log', level=log.INFO, datefmt='%Y-%m-%d, %H:%M:%S')
    log.info("|--------- SIP SERVER ----------")
    log.info("| START TIME: " + t.strftime("%a, %d %b %Y %H:%M:%S ", t.localtime()))
    host_name = socket.gethostname()
    log.info("| SERVER HOST NAME: " + host_name)

    server_address = socket.gethostbyname(host_name)
    if server_address == "127.0.0.1" and len(sys.argv) > 1:
        server_address = sys.argv[1]
    else:
        server_address = input("Please enter server IP!!\n")

    sip.recordroute = "Record-Route: <sip:%s:%d;lr>" % (server_address, sip.PORT)
    sip.topvia = "Via: SIP/2.0/UDP %s:%d" % (server_address, sip.PORT)
    sip_server = ss.UDPServer((sip.HOST, sip.PORT), sip.UDPHandler)

    print("SERVER: " + str(server_address) + " IS RUNNING ON PORT: " + str(sip.PORT))
    log.info("| SERVER: " + str(server_address) + " IS RUNNING ON PORT: " + str(sip.PORT))
    sip_server.serve_forever()

if __name__ == "__main__":
    runSIP()