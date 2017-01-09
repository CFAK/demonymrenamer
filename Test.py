import json
import requests
import os
import re

FILE_EXTENSION = ".png"

def getDemonym(countryName):
    url = "https://restcountries-v1.p.mashape.com/name/" + countryName
    header={ "X-Mashape-Key": "q99HjRn1x8mshKUqu0L2HJwgQhmUp1rSGDkjsnLvbmVw6rXDfm", "Accept": "application/json"}
    t = requests.get(url, headers=header)
    if t.status_code == 404:
        print("Error Trying to Find", countryName)
        return countryName

    newDictionary=json.loads(t.content)
    return str(newDictionary[0]['demonym'])

def driver():

    FILE_PATH = 'Flag_Nationalities'


    for fileName in os.listdir(FILE_PATH):
        countryName = str(fileName)
        countryName = re.sub(r'_', ' ', countryName)
        demonym = getDemonym(countryName.replace(FILE_EXTENSION,''))



        oldFileName = os.path.join(FILE_PATH, str(fileName))

        newFileName = os.path.join(FILE_PATH, str(demonym)+FILE_EXTENSION)

        print newFileName

        # os.rename("Albania.png","Albanian.png")
        os.rename(oldFileName,newFileName)

driver()
