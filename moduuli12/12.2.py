import requests
import json
apikey="f7aaa3944838d9fd94bed74be2d38db0"



haku = input("Anna paikkakunta: ")

kelv= requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={haku}&appid={apikey}").json()
cels=(kelv["main"]["temp"])-272.15

koord=requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={haku}&limit=5&appid={apikey}").json()
#print(json.dumps(koord, indent=2))
lat=(koord[0]["lat"])
lon=(koord[0]["lon"])

sää = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}").json()
#print(json.dumps(sää, indent=2))
kuvailu=(sää["weather"][0]["description"])
print(f"Paikkakuntalla {haku} säätila on {kuvailu}.\nJa lämpötila on {cels} celsiusta")


