import urllib.request
import requests
import threading
import json

import random

""" https://api.thingspeak.com/channels/1178345/fields/1.json?api_key=XIYH8HRWEAXH82ZK&results=2
"""

def read_data_thingspeak():
 
    URL='https://api.thingspeak.com/channels/1178345/fields/1.json?api_key'
    KEY='XIYH8HRWEAXH82ZK'
    HEADER='&results=2'
    NEW_URL=URL+KEY+HEADER
    print(NEW_URL)

    get_data=requests.get(NEW_URL).json()
    #print(get_data)
    channel_id=get_data['channel']['id']

    field_1=get_data['feeds']
    #print(field_1)

    t=[]
    for x in field_1:
        print(x['field1'])
        t.append(x['field1'])

if __name__ == '__main__':
    #thingspeak_post()
    read_data_thingspeak()