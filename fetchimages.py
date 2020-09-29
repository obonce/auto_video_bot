#!/usr/bin/python

import sys
import requests

class ImageFetcher:
    def __init__(self):
        self.__pixabayApiKey = "18373041-7bf8693b82f9f455531b64921"
        self.__pixabayEndpoint = "https://pixabay.com/api/"

    def __appendApiKey(self, pixabayUrl):
        return pixabayUrl + '&key=' + self.__pixabayApiKey

    def fetchImages(self, nicheName):
        fetchUrl = self.__appendApiKey(self.__pixabayEndpoint + "?q=" + nicheName)
        result = requests.get(fetchUrl)
        print(result.json())



# Get niche name as input from user
argsLength = len(sys.argv)

if argsLength != 2:
    print('Need one more argument')
    sys.exit()
    
imageFetcher = ImageFetcher()
imageFetcher.fetchImages(sys.argv[1])