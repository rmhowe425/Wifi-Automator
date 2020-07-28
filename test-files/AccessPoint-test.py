import unittest
from Src.Wifi import WiFi

class MyTestCase(unittest.TestCase):
    def test_initAndSetMethods(self):
        wifi_inst = WiFi()
        ap = wifi_inst.AccessPoint('A', 'A', 0, 0)

        self.assertEqual(ap.MAC, 'A')
        self.assertEqual(ap.SSID, 'A')
        self.assertEqual(ap.dBm, 0)
        self.assertEqual(ap.channel, 0)
        self.assertEqual(ap.handshake, False)

if __name__ == '__main__':
    unittest.main()
