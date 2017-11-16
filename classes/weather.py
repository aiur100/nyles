import json
import urllib.request

class Weather:
	weatherUrl = "https://api.darksky.net/forecast"

	def __init__(self,apiKey,latit = 39.960664,long = -75.605488):
		self.long 			= long
		self.latit  		= latit
		longString  		= str(long)
		latString   		= str(latit)
		self.apiKey 		= apiKey
		self.weatherUrl  	= self.weatherUrl+"/"+apiKey+"/"+latString+","+longString

	def getWeatherData(self):
		self.data = json.loads(urllib.request.urlopen(self.weatherUrl).read())	

	def verifyCachedWeatherData(self):
		if hasattr(self, 'data') is False:
			self.getWeatherData()

	def getCurrentlyData(self):
		self.verifyCachedWeatherData()
		return self.data['currently']	

	def getDailyData(self):
		self.verifyCachedWeatherData()
		return self.data['daily']

	def currentSummary(self):
		return self.getCurrentlyData()['summary']

	def currentTemperature(self):
		return self.getCurrentlyData()['temperature']

	def dailySummary(self):
		return self.getDailyData()['summary']		
		

