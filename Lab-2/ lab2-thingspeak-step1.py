import http.client as httplib
import urllib.parse as urllib 
import time

import my_pi_emulator_1 as pEmu


Temp = pEmu.tempMod()

key = "XIYH8HRWEAXH82ZK"  # Put your API Key here
def thermometer():
    while True:
        #Calculate CPU temperature of Raspberry Pi in Degrees C
        #temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp

        #in the absense of rpi,use imported pi emulator
        temp = Temp.readC()
        
        params = urllib.urlencode({'field1': temp, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print(temp)
            print("{},{}".format(response.status, response.reason))
            data = response.read()
            conn.close()
        except:
            print("connection failed")
        break
if __name__ == "__main__":
        while True:
                thermometer()