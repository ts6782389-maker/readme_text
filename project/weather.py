import requests

responses = requests.get("https://api.open-meteo.com/v1/forecast?latitude=28.6&longitude=77.2&current_weather=true")
data = responses.json()
current = data["current_weather"]["temperature"]
print(current)

city = input('enter your city')
geo_respone = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}")
geo_data = geo_respone.json()
print(geo_data)

lat = geo_data["results"][0]["latitude"]
lon = geo_data["results"][0]["longitude"]
print(lat,lon)

weather_response = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true")
weather_data = weather_response.json()
temp = weather_data["current_weather"]["temperature"]
print(f"The temperature in {city} is {temp}°C")