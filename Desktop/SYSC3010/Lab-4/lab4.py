import requests
import urllib.request
import json

URL = 'https://api.thingspeak.com/update/?api_key='
KEY = '7481QW0APO2BO2BU'
HEADER = '&field1={L1-F-2}&field2={d}&field3={seyisehindeibini@cmail.carleton.ca}'
NEWURL = URL+KEY+HEADER
print(NEWURL)

data = urllib.request.urlopen(NEWURL)
print(data)
