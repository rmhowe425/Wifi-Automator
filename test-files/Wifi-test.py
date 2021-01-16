import unittest
from Src.Wifi import WiFi
from util.IO import IO
'''
    Unit test for the Wifi class.
    [*] TESTS MUST BE RAN AS ROOT [*]
    --> Must be root to set wireless NIC to monitor mode <--
'''
class MyTestCase(unittest.TestCase):

    '''
        Tests the constructor for the WiFi class.
    '''
    def test_init(self):
        inst = WiFi()

        self.assertEqual(inst.tCount, 99)
        self.assertEqual(len(inst.SSIDs), 0)
        self.assertFalse(inst.done)
        self.assertEqual(len(inst.buff), inst.tCount)

        for item in inst.buff:
            self.assertEqual(item, '')


    '''
        Tests the setMonMode method in the WiFi class.
    '''
    def test_SetMonMode(self):
        inst = WiFi()

        config = IO.readConfigFile()
        self.assertEqual(config['[Adapter]'], inst.setMonMode(config['[Adapter]']))



if __name__ == '__main__':
    unittest.main()
