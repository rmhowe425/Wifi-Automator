from pcap import pcapObject
from socket import socket, AF_PACKET, SOCK_RAW

'''
    Class responsible for all socket and I/O operations. 
'''
class IO:

    def deAuth(self, NIC):
        pc.open_offline("/artifacts/deauth.pcap")
        packet_file = open("deauth.pcap")
        s.bind((NIC))

        deauth = pc.next()

