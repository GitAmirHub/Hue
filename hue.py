from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import ssl

discovery_url = 'https://discovery.meethue.com/' #used to get ip address of bridge incase it changes (dynamic)
my_url = 'https://192.168.1.104/debug/clip.html' #url of bridge, currently. Will change to be automated from discovery_url later
user = '7vZqfGXI17ej986DZw1azmHM2pEd9j4Boa5H3qdQ' #Registered user so does not need to authenticate every time

uClient = uReq(my_url, context=ssl._create_unverified_context())
page_html = uClient.read() #reads the page and stores it
uClient.close() #closes the reader
page_soup = soup(page_html, "html.parser") #creates a soup of the page in html


#Gets the lights info and prints to terminal
def getLightInfo():
    #Modifies the input box to add the user for authentication
    user_tag = page_soup.input
    user_tag['value'] = '/api' + user
    pass

#Turns the bedroom light on
def lightOn():
    pass

#Turns the bedroom light off
def lightOff():
    pass

#Sets the bedroom light colour
def setColour(rgb):
    pass

#Sets the bedroom light brightness
def setBrightness(brightness):
    pass