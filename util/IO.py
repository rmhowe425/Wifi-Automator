from datetime import datetime

'''
    Class responsible for all file I/O operations. 
'''
class IO:

    '''
        Writes packets to a file.
        3-way handshake should be included.
        @param data: Data containing the 3-way handshake. 
                     Data may be a scapy instance.
    '''
    def writeFile(self, data):
        return

    '''
        Writes an error message to a log file.
        Each entry has the date and time and is 
        appended to the same file.
        @param error: Error message to be logged.
        @param path: File path to the file to be written to.  
    '''
    def writeToErrorLog(error):
        file = open('../artifacts/Error Log.txt', 'a+')
        timestamp = ''.join([datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), '\n', '-' * 20, '\n'])

        file.write(timestamp + error + '\n\n')
        file.close()

    '''
        Used to clear the error log during testing. 
    '''
    def clearErrorLog(self):
        file = open('../artifacts/Error Log.txt', 'w')
        file.close()