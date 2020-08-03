from os import geteuid
from util.IO import IO
from netifaces import interfaces
from subprocess import Popen, PIPE
from scapy.all import sniff, rdpcap, send
from socket import socket, AF_PACKET, SOCK_RAW


''' 
    Class responsible for automating the process of recording 
    access point information and capturing WPA2 handshakes.
'''
class WiFi:

    '''
        Constructor for the WiFi class.
    '''
    def __init__(self):
        self.NICs = []
        self.SSIDs = {}
        self.device = ''

    '''
        Searches for all available NIC's and returns
        a list of NIC's that can be used in monitor mode.
    '''
    def scanAdapters(self):
        nic = []

        for dev in interfaces():
            if 'lo' not in dev and 'eno' not in dev and 'vm' not in dev:
                nic.append(dev)
        self.NICs = nic

    '''
        Parses the list of available NIC's and sets the
        first available device to monitor mode. 
        Sets the value of self.NIC to the name of the NIC
        in monitor mode. 
        @return: Boolean value representing success of method execution.
    '''
    def setMonMode(self):
        success = False

        if geteuid() != 0:
            IO.writeToErrorLog('You must run this program as root.')
            return success

        for dev in self.NICs:
            try:
                # Shut down the device
                msg = Popen(['ifconfig', dev, 'down'], stderr = PIPE)
                msg.communicate() # Not saving output.

                # Attempt to put device in monitor mode
                msg = Popen(['iwconfig', dev, 'mode', 'monitor'], stderr = PIPE)
                msg.communicate() # Not saving output.

                self.device = dev
                success = True
                break

            except Exception as e:
                IO.writeToErrorLog(e)
            return success

        '''
            Sends a spoofed deauth packet from the client (CLI) to the access point
            (AP) in order to generate a 3-way handshake upon reconnection.
            @param: AP: Access point that receives the deauth packet.
            @param CLI: Client that will be deauthenticated from the access point.
            @param NIC: Network card to send the deauth packet on.
            @return: Boolean value representing the success of the method.
        '''
        def sendDeauth(self, AP, CLI, NIC):
            file = rdpcap('../artifacts/deauth.pcap')
            packet = socket(AF_PACKET, SOCK_RAW)

            # TODO Fill in SSID, AP, CLI MAC fields of deauth packet




