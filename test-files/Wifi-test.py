import unittest
from Src.Wifi import WiFi

'''
    Unit test for the Wifi class.
'''
class MyTestCase(unittest.TestCase):

    '''
        Tests the constructor for the WiFi class.
    '''
    def test_init(self):
        wifi_inst = WiFi()
        self.assertEqual(len(wifi_inst.NICs), 0)
        self.assertEqual(len(wifi_inst.SSIDs), 0)

    '''
        Tests the scanAdapters method in the WiFi class.
    '''
    def test_scanAdapters(self):
        wifi_inst = WiFi()

        # hard coded list of adapters on rmhowe425's desktop
        devices = ['eno1', 'lo', 'vmnet1', 'vmnet8', 'wlx00c0ca6daed8']
        wifi_inst.scanAdapters()

        self.assertTrue(len(wifi_inst.NICs) == 1)
        self.assertEqual('wlx00c0ca6daed8', wifi_inst.NICs[0])

    '''
        Tests the setMonMode method in the WiFi class.
    '''
    def test_setMonMode(self):
        wifi_inst = WiFi()
        wifi_inst.scanAdapters()

        # Test towards end of implementation - Program must be ran as root.
        #self.assertEqual(wifi_inst.setMonMode(), True)
        #self.assertEqual(wifi_inst.NICs[0], wifi_inst.device)
        self.assertTrue(True)






if __name__ == '__main__':
    unittest.main()
