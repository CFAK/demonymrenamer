import unirest
import simplejson as json

def getDemonym(countryName):
    response = unirest.get("https://restcountries-v1.p.mashape.com/name/" + countryName,
        headers={
            "X-Mashape-Key": "q99HjRn1x8mshKUqu0L2HJwgQhmUp1rSGDkjsnLvbmVw6rXDfm",
            "Accept": "application/json"
        }
    )
    data = response.raw_body
    print (data)
    jsond=json.load(data)
    # print(jsond['demonym'])


# def changeFileName(oldValue,newValue):

def driver():
    # countryName = raw_input('Enter a Country: ')
    # print("Input is working:",countryName)
    demonym = getDemonym("Germany")
    # print(demonym)
    print("Hi")

driver()
