import requests
import json
city = input("Enter city name:")

api_key = "4456508fa52256c145a799ed99246fea"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)
data = response.json()

temperature = data['main']['temp']
humidity = data['main']['humidity']
weather = data['weather'][0]['description']

print("\nWeather Details")
print("City:", city)
print("Temperature:", temperature, "°C")
print("Humidity:", humidity, "%")
print("Condition:", weather)

