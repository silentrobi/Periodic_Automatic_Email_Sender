import json
from urllib.request import urlopen

class JsonLoader:

    def __init__(self):
        self.__jsonData= {}


    def loadJsonData(self, url):
        try:
            urlLoader = urlopen(url)
            self.__jsonData= json.load(urlLoader)
        except Exception as e:
            print(e)
    def getJsonData(self):
        return self.__jsonData


