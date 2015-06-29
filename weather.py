import requests, json
import pyowm

'''
I'm using openweathermap.org
Example of API call:
api.openweathermap.org/data/2.5/forecast/city?id=524901&APPID=1111111111
'''
API_KEY = 'a0fa273bad0cf14641777cc227165163'  # Your OWM API KEY

class Weather(object):
  """docstring for """

  def __init__(self):
    self.owm = pyowm.OWM(API_KEY)
    self.weather = None
    self.wind = None
    self.humidity = None
    self.temp = None
    self.status = None

  def get_observation(self, city):
    return self.owm.weather_at_place(city)

  def update_humidity(self):
    self.humidity = self.weather.get_humidity()

  def update_wind(self):
    ''' Returns [speed, degree] '''
    self.wind = self.weather.get_wind().values()

  def update_temp(self):
    self.temp = self.weather.get_temperature('celsius')['temp']

  def update_status(self):
    self.status = self.weather.get_status()

  def update_weather(self, city):
    self.weather = self.get_observation(city).get_weather()

  def update(self, city):
    self.update_weather(city)
    self.update_humidity()
    self.update_wind()
    self.update_temp()
    self.update_status()

#w = Weather()
#w.update('new york')
#w.humidity
#print 'Humidity: %d%%' % w.humidity
#print w.temp
#print w.weather.get_status()
#seoul = Weather()
#print seoul.get_temperature('Seoul')
#print seoul.get_temperature('Seoul')['temp']
