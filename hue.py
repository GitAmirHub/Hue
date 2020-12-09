#from urllib.request import urlopen as uReq
#from bs4 import BeautifulSoup as soup
#import ssl
import requests
from requests.models import Response

"""Old method was going to use web scraping to input the json commands and exectue, however I did not want to use Selenium to 
click on the get/put buttons etc. Ended up using requests to request json queries which works well for simple hue commands."""

""" discovery_url = 'https://discovery.meethue.com/' #used to get ip address of bridge incase it changes (dynamic)
my_url = 'https://192.168.1.104/debug/clip.html' #url of bridge, currently. Will change to be automated from discovery_url later
user = '7vZqfGXI17ej986DZw1azmHM2pEd9j4Boa5H3qdQ' #Registered user so does not need to authenticate every time

uClient = uReq(my_url, context=ssl._create_unverified_context())
page_html = uClient.read() #reads the page and stores it
uClient.close() #closes the reader
page_soup = soup(page_html, "html.parser") #creates a soup of the page in html """


#Gets the lights info and prints to terminal
def getLightInfo():
    headers = {
        'Accept': 'application/json',
    }
    data = ''
    response = requests.get('http://192.168.1.104/api/7vZqfGXI17ej986DZw1azmHM2pEd9j4Boa5H3qdQ/lights', headers=headers, data=data)
    response.raise_for_status()
    jsonResponse = response.json()
    print(jsonResponse)

#Turns the bedroom light on
def lightOn():
    headers = {
        'Accept': 'application/json',
    }
    data = '{"on": true,"bri": 254,"hue": 8402,"sat": 140,"effect": "none"}'
    response = requests.put('http://192.168.1.104/api/7vZqfGXI17ej986DZw1azmHM2pEd9j4Boa5H3qdQ/lights/2/state', headers=headers, data=data)
    response.raise_for_status()
    jsonResponse = response.json()
    print(jsonResponse)
    

#Turns the bedroom light off
def lightOff():
    headers = {
    'Accept': 'application/json',
    }
    data = '{"on":false}'
    response = requests.put('http://192.168.1.104/api/7vZqfGXI17ej986DZw1azmHM2pEd9j4Boa5H3qdQ/lights/2/state', headers=headers, data=data)
    response.raise_for_status()
    jsonResponse = response.json()
    print(jsonResponse)

#Sets the bedroom light colour
def setColour(rgb):
    pass

#Sets the bedroom light brightness
def setBrightness(brightness):
    pass