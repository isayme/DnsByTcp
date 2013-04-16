import os, sys
import socket
import struct
import threading
import SocketServer
import random

# DNS Server List
DNS_SERVS = ['8.8.8.8',
         '8.8.4.4',
         '208.67.222.222',
         '208.67.220.220',
         ]

DNS_PORT = 53           # default dns port 53
TIMEOUT = 20            # set timeout 5 second

def QueryDnsByTcp(dns_ip, dns_port, query_data):
    # make TCP DNS Frame
    tcp_frame = struct.pack('!h', len(query_data)) + query_data
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(TIMEOUT) # set socket timeout
        s.connect((dns_ip, dns_port))
        s.send(tcp_frame)
        data = s.recv(2048)
    except:
        if s: s.close()
        return
      
    if s: s.close()
    return data

class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    # Ctrl-C will cleanly kill all spawned threads
    daemon_threads = True
    # much faster rebinding
    allow_reuse_address = True
    
    def __init__(self, s, t):
        SocketServer.UDPServer.__init__(self, s, t)

class ThreadedUDPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        query_data = self.request[0]
        udp_sock = self.request[1]
        addr = self.client_address

        dns_ip = DNS_SERVS[random.randint(0, len(DNS_SERVS) - 1)]
        response = QueryDnsByTcp(dns_ip, DNS_PORT, query_data)
        if response:
            # udp dns packet no length
            udp_sock.sendto(response[2:], addr)
        
        
if __name__ == "__main__":
    print "---------------------------------------------------------------"
    print "| To Use this tool, you must set your dns server to 127.0.0.1 |"
    print "---------------------------------------------------------------"
    
    dns_server = ThreadedUDPServer(('127.0.0.1', 53), ThreadedUDPRequestHandler)
    dns_server.serve_forever()
