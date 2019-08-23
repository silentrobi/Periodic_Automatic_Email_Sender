import json
from urllib.request import urlopen

class JsonLoader:

    def __init__(self):
        self.__jsonData= {}


    def loadJsonData(self, url):
        urlLoader = urlopen(url)
        self.__jsonData= json.load(urlLoader)
    def getJsonData(self):
        return self.__jsonData


