import configparser

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")

class ReadConfig:

    @staticmethod
    def getURL():
        url = config.get('common info', 'baseURL')
        return url