import requests
from datetime import datetime

#API Key from OpenWeatherMap
API_KEY = '3470ff8888f7179ffa2af14184fa7276'
CITY = 'Vancouver'
COUNTRY = 'CA'
WEATHER_URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY},{COUNTRY}&appid={API_KEY}&units=metric"
TIME_URL = "http://worldtimeapi.org/api/timezone/America/Vancouver"

def get_weather():
    response = requests.get(WEATHER_URL)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        return temp
    else:
        print("Error - unable to fetch weather data")
        return None

def get_time():
    response = requests.get(TIME_URL)
    if response.status_code == 200:
        data = response.json()
        datetime_str = data['datetime']
        current_time = datetime.fromisoformat(datetime_str).strftime('%Y-%m-%d %H:%M:%S')
        return current_time
    else:
        print("Error - unable to fetch time data")
        return None

if __name__ == "__main__":
    temperature = get_weather()
    current_time = get_time()

    if temperature is not None and current_time is not None:
        print()
        print(f"The current temperature in Vancouver, BC is: {temperature}°C")
        print(f"The current time in Vancouver, BC is: {current_time}")
        print()
    else:
        print("Error - failed to retrieve weather or time data.")
