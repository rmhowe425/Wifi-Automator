import unittest
from Src.Wifi import AccessPoint

class MyTestCase(unittest.TestCase):

    def test_Constructor(self):
        inst = AccessPoint('MAC', 'SSID', -50, 11)

        # Check initial constructor values
        self.assertEqual(inst.MAC, 'MAC')
        self.assertEqual(inst.SSID, 'SSID')
        self.assertEqual(inst.dBm, -50)
        self.assertEqual(inst.channel, 11)
        self.assertEqual(inst.handshake, False)



if __name__ == '__main__':
    unittest.main()
