from netifaces import interfaces

class WiFi:

    def __init__(self):
        self.SSIDs = {}
        self.NICs  = []

    def scanAdapters(self):
        nic = []

        for dev in interfaces:
            if 'lo' not in dev and 'eno' not in dev and 'vm' not in dev:
                nic.append(dev)
        return nic

    def setMonMode(self):
        return

    def enumSSID(self):
        return

    def deAuth(self):
        return

    class AccessPoint:

        def __init__(self, MAC, SSID, dBm, channel):
            self.MAC = self.SetMAC(MAC)
            self.SSID = self.SetSSID(SSID)
            self.dBm = self.SetdBm(dBm)
            self.channel = self.setChannel(channel)
            self.handshake = False

        def SetMAC(self, MAC):
            # Future work for potential string verification
            return MAC
        
        def SetSSID(self, SSID):
            # Future work for potential string verification
            return SSID
        
        def SetdBm(self, dBm):
            # Future work for number verification
            return dBm

        def setChanel(selfself, channel):
            # Future work for number verification
            return channel

        def setHandshake(self):
            self.handshake = not self.handshake
