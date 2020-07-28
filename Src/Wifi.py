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



    '''
        Class responsible for maintaining a record of information
        for each visible access point. 
    '''
    class AccessPoint:

        '''
            Constructor for the AccessPoint inner class.
            @param MAC: MAC address of an access point.
            @param SSID: Visible name of the access point.
            @param dBm: Strength of the signal of the access point.
            @param channel: Channel # that the access point is running on.
        '''
        def __init__(self, MAC, SSID, dBm, channel):
            self.MAC = self.SetMAC(MAC)
            self.SSID = self.SetSSID(SSID)
            self.dBm = self.SetdBm(dBm)
            self.channel = self.setChannel(channel)
            self.handshake = False

        '''
            Records the MAC address 
            @param: MAC: MAC address of the access point.
            @return: String containing the MAC address of the access point. 
        '''
        def SetMAC(self, MAC):
            # Future work for potential string verification
            return MAC

        '''
            Records the SSID name of the access point.
            @param SSID: Visible name of the access point.
            @return: String containing the SSID of the access point.
        '''
        def SetSSID(self, SSID):
            # Future work for potential string verification
            return SSID

        '''
            Records the strength of the access point.
            @param: dBm: Integer value of the strength of the access point. 
            @return: Integer value containing the strength of the access point. 
        '''
        def SetdBm(self, dBm):
            # Future work for number verification
            return dBm

        '''
            Records the channel that the access point is operating on.
            @param: channel: Integer containing the channel that the access point is operating on.
            @return: Integer value containing the channel that the access point is operating on. 
        '''
        def setChannel(selfself, channel):
            # Future work for number verification
            return channel

        '''
            Sets self.handshake to True when a handshake is captured.
            Should only be called once.
        '''
        def setHandshake(self):
            self.handshake = not self.handshake
