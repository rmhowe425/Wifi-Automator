from datetime import datetime

'''
    Class responsible for all file I/O operations. 
'''
class IO:

    @staticmethod
    def readConfigFile():
        file_path = '../artifacts/wifi.config'
        config = {'[Adapter]': '', '[Whitelist]': ''}

        file = open(file_path, 'r')
        contents = file.read().split("\n")

        for i in range(len(contents)):
            if contents[i] == '[Adapter]':
                config['[Adapter]'] = contents[i + 1].strip()
            elif contents[i] == '[Whitelist]':
                config['[Whitelist]'] = contents[i + 1].strip()

        file.close()
        return config

    '''
        Writes an error message to a log file.
        Each entry has the date and time and is 
        appended to the same file.
        @param error: Error message to be logged.
    '''
    @staticmethod
    def writeToErrorLog(error):
        flag = True
        timestamp = ''.join([datetime.today().strftime('%Y-%m-%d-%H:%M:%S'), '\n', '-' * 20, '\n'])

        try:
            file = open('../artifacts/Error Log.txt', 'a+')
            file.write(timestamp + error + '\n\n')
            file.close()
        except IOError:
            flag = False

        return flag
