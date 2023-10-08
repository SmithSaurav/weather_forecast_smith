import re
import json
import requests
url = 'http://ip-api.com/json'
response = requests.get(url)
data = response.json()

IP=data['query']
org=data['org']
city = data['city']
country=data['country']
region=data['region']
print(data)
# print 'Your IP detail\n '
# print 'IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP)


queryUrl = "https://api.openweathermap.org/data/2.5/onecall?"
# lat = "lat=52.229676&"
# lon = "lon=21.012229&"
# lat = f"lat={data['loc'].split(',')[0]}&"
# lon = f"lon={data['loc'].split(',')[0]}&"
apiOptions = "units=metric&exclude=minutely,alerts&"
apiKey = "appid=dbb76c5d98d5dbafcb94441c6a10236e"
file = queryUrl + lat + lon + apiOptions + apiKey
response = requests.get(file)
data_new = response.json()
main = data_new['current']['weather'][0]['main']
description = data_new['current']['weather'][0]['description']
temp = round(data_new['current']['temp'])
pressure = data_new['current']['pressure']
humidity = data_new['current']['humidity']
print(main,description,temp,pressure,humidity)
print(data_new)
print("done")
