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
        self.MAC = self.setMAC(MAC)
        self.SSID = self.setSSID(SSID)
        self.dBm = self.setdBm(dBm)
        self.channel = self.setChannel(channel)
        self.handshake = False

    '''
        Records the MAC address 
        @param: MAC: MAC address of the access point.
        @return: String containing the MAC address of the access point. 
    '''
    def setMAC(self, MAC):
        # Future work for potential string verification
        return MAC

    '''
        Records the SSID name of the access point.
        @param SSID: Visible name of the access point.
        @return: String containing the SSID of the access point.
    '''
    def setSSID(self, SSID):
        # Future work for potential string verification
        return SSID

    '''
        Records the strength of the access point.
        @param: dBm: Integer value of the strength of the access point. 
        @return: Integer value containing the strength of the access point. 
    '''
    def setdBm(self, dBm):
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
        self.handshake = True
