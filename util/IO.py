from datetime import datetime

'''
    Class responsible for all file I/O operations. 
'''
class IO:

    '''
        Writes an error message to a log file.
        Each entry has the date and time and is 
        appended to the same file.
        @param error: Error message to be logged.
    '''
    @staticmethod
    def writeToErrorLog(error):
        file = open('../artifacts/Error Log.txt', 'a+')
        timestamp = ''.join([datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), '\n', '-' * 20, '\n'])

        file.write(timestamp + error + '\n\n')
        file.close()

    '''
        Used to clear the error log during testing. 
    '''
    @staticmethod
    def clearErrorLog(self):
        file = open('../artifacts/Error Log.txt', 'w')
        file.close()