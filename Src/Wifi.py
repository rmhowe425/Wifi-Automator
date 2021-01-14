from pcap import pcap
from os import geteuid
from util.IO import IO
from threading import Thread
from subprocess import Popen, PIPE
from Src.AccessPoint import AccessPoint
from Src.radtiotap.radiotap import radiotap_parse, ieee80211_parse

''' 
    Class responsible for automating the process of recording 
    access point information and capturing WPA2 handshakes.
'''
class WiFi:

    '''
        Constructor for the WiFi class.
        @param nic: Network Interface to sniff on
    '''
    def __init__(self):
        self.tCount = 99
        self.SSIDs = {}
        self.done = False
        self.buff = [''] * self.tCount
        self.NICs = self.scanAdapters()

    '''
        Parses the list of available NIC's and 
        sets a specified device to monitor mode.
        @param nic: Specified device to be set to monitor mode. 
        @return: Name of device set to monitor mode. 
    '''
    def setMonMode(self, nic):
        device = ''

        # Make sure that the script is running as root(Needs to be able to perform packet injection).
        if geteuid() != 0:
            IO.writeToErrorLog('You must run this program as root.')

        else:
            for dev in self.NICs:
                if dev is nic:
                    try:
                        # Shut down the device
                        msg = Popen(['ifconfig', dev, 'down'], stderr = PIPE)
                        msg.communicate() # Not saving output.

                        # Attempt to put device in monitor mode
                        msg = Popen(['iwconfig', dev, 'mode', 'monitor'], stderr = PIPE)
                        msg.communicate() # Not saving output.

                        device = dev
                        break
                    except Exception as e:
                        IO.writeToErrorLog(e)
        return device

    '''
        Filters and stores packets based on specified properties.
        [*] This method is intended to be ran on multiple dedicated threads.
        @param Id: Unique identifier given to a single thread. 
    '''
    def filterPacket(self, Id):
        packet = self.buff[Id]
        while True:

            # Done criteria, kill thread.
            if self.done:
                break

            # worker thread needs to wait.
            elif self.buff[Id] == packet:
                pass

            # Parse and record packet information.
            else:
                packet = self.buff[Id]
                offset, rt_data = radiotap_parse(packet)

                # Broadcast-type of packet (signifies an access point)
                if packet[offset] == 0x80:
                    iEE_offset, ap_info = ieee80211_parse(packet, offset)
                    start = iEE_offset + 14

                    # SSID
                    ssid = (packet[start: start + packet[iEE_offset + 13]]).decode()
                    # Power
                    pwr = rt_data['dbm_antsignal']
                    # MAC address
                    mac = ap_info['addr3']

                    # Add new item to dictionary
                    if ssid not in self.SSIDs:
                        self.ap_list[ssid] = AccessPoint(pwr, mac, ssid)

    '''
        Method used for sniffing packets. 
        [*] This method is intended to be ran in a dedicated thread 
            for the entire duration of program execution.
        @param nic: Device to sniff packets on.
    '''
    def sniff(self, nic):
        Id = 0
        sniff = pcap(name=nic, snaplen=65535, promisc=True, immediate=True)
        thread_pool = [Thread(target = self.filterPacket, name=i) for i in range(0, self.tCount)]

        # Execute threads
        for worker in thread_pool:
            worker.start()

        try:
            while True:
                self.buff[Id] = sniff.__next__()[1]
                Id = (Id + 1) % 10

        except KeyboardInterrupt:
            for worker in thread_pool:
                worker.thread.join()
            return None