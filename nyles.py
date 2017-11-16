from subprocess 		import call
from classes.assistant	import Assistant
from classes.weather	import Weather
import json

keys  = json.loads(open("keys/api_keys.json").read())
nyles = Assistant("Nyles")

#nyles.greeting()
#nyles.pendingRequestMessage()


weather = Weather(keys['darkSky'])

nyles.say("The weather is currently "+weather.currentSummary()
	+" with a temperature of "
	+str(weather.currentTemperature())
	+"degrees")

nyles.say("The daily weather summary is "+weather.dailySummary())




