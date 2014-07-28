import json 
import urllib2
def get_temperature():
	city = 'Delft'
	# get weather JSON data using OpenWeatherMap API
	urlstr = "http://api.openweathermap.org/data/2.5/weather?q={}".format(city)
	x = urllib2.urlopen(urlstr).read()
	# parse URL data as JSON
	y = json.loads(x)
	# Get temperature data from decoded JSON
	temperature = y['main']['temp'] - 273.15
	return temperature
