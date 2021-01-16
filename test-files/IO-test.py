import unittest
from util.IO import IO

'''
    Tests the functionality of the static methods in the IO class.
'''
class MyTestCase(unittest.TestCase):

    '''
        Tests the functionality of the readConfigFile method.
    '''
    def test_ReadConfigFile(self):
        output = IO.readConfigFile()

        # Verify correct length of output
        self.assertTrue(2, len(output))

        # Verify correct Wi-Fi NIC is detected
        self.assertEqual(output.get('[Adapter]'), 'wlx00c0ca6daed8')

        # Verify that no SSID's are whitelisted by default
        self.assertEqual(output.get('[Whitelist]'), '')


    def test_WriteToErrorLog(self):
        # Write to error log once
        self.assertTrue(IO.writeToErrorLog("Test0"))

        #Write to error log ten times
        for i in range(1, 11):
            self.assertTrue(IO.writeToErrorLog("Test{}".format(i)))


if __name__ == '__main__':
    unittest.main()
