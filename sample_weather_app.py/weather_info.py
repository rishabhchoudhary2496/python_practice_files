import requests
from requests.exceptions import HTTPError
from gtts import gTTS
import os
import random

class Weather():
    '''
    Returns Weather Report 
    '''
    API_KEY = '7e16d6f9cf94d797f62e17eeb3d8fbf7'
    BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

    def __init__(self,lat,long) -> None:
        self.lat = lat
        self.long = long
    
    @staticmethod
    def format_weather(weather_report) -> dict:
        '''
            input - Dictionary object
            output - Dictionary object

        Description - Takes a weather dictionary and format information nicely
        '''
        weather_info = weather_report['weather'][0] | weather_report['main']
        weather_info['wind'] = weather_report['wind']
        return weather_info

    @staticmethod
    def listen_report(weather_report):
        output = gTTS(text=weather_report,lang='en',slow=False)
        file_name = f'weather_report-{random.randrange(1,10000000)}.mp3'
        output.save(file_name)
        os.system(f'start {file_name}')

    @staticmethod
    def make_report(weather_info):
        return f"it's a {weather_info['description']} and humidity is {weather_info['humidity']} wind is blowing at the speed of {weather_info['wind']['speed']} km per hour"

    def get_weather(self):
        try:
            rawData = requests.get(f'{Weather.BASE_URL}?lat={self.lat}&lon={self.long}&appid={Weather.API_KEY}')
            jsonData = rawData.json() 
            return jsonData
        except HTTPError as error:
            print('Error',error)
            



weather = Weather('30.741482','76.768066')
weather_data = weather.get_weather()
weather_info = Weather.format_weather(weather_data)
weather_report = Weather.make_report(weather_info)
Weather.listen_report(weather_report)


