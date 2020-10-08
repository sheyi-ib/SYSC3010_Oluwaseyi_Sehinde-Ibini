from urllib.request import * 
from urllib.parse import * 
import json

import sqlite3

# The URL that is formatted: http://api.openweathermap.org/data/2.5/weather?APPID=a808bbf30202728efca23e099a4eecc7&units=imperial&q=ottawa


# As of October 2015, you need an API key.
# I have registered under my Carleton email.
apiKey = "a808bbf30202728efca23e099a4eecc7"

# Query the user for a city
city = input("Enter the name of a city whose weather you want: ")

# Build the URL parameters
params = {"q":city, "units":"imperial", "APPID":apiKey }
arguments = urlencode(params)

# Get the weather information
address = "http://api.openweathermap.org/data/2.5/weather"
url = address + "?" + arguments

print (url)
webData = urlopen(url)
results = webData.read().decode('utf-8')
  # results is a JSON string
webData.close()

print (results)
#Convert the json result to a dictionary
# See http://openweathermap.org/current#current_JSON for the API

data = json.loads(results)

# Print the results

current = data["main"]
degreeSym = chr(176)

print ("Temperature: %d%sF" % (current["temp"], degreeSym ))
print ("Humidity: %d%%" % current["humidity"])
print ("Pressure: %d" % current["pressure"] )

current = data["wind"]
print ("Wind : %d" % current["speed"])


print("\n ===== STARTING DB OPERATIONS ON WIND_SPEED TABLE ===== \n");

dbconnect = sqlite3.connect("my.db");
dbconnect.row_factory = sqlite3.Row;
cursor = dbconnect.cursor();

try:
    cursor.execute('''create table city_wind_speed(city text, ws text)''');
except sqlite3.OperationalError:
    pass

cursor.execute('''insert into city_wind_speed values (?, ?)''',
               (city, current["speed"]));


dbconnect.commit();

#display all the sensors in the kitchen
print("\r\n\n -- all city wind speed -- \n");
cursor.execute('SELECT * FROM city_wind_speed');
#print data
for row in cursor:
    print(row['city'],row['ws']);

#close the connection
dbconnect.close();