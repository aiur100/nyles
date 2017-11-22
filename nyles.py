from subprocess 		import call
from classes.assistant	import Assistant
from classes.weather	import Weather
import speech_recognition as sr
import json
import pyaudio,os
import hashlib

keys  	= json.loads(open("keys/api_keys.json").read())
google 	= open("keys/my-google-cloud-speech-credentials.json").read()
weather = Weather(keys['darkSky'])
nyles 	= Assistant("Nyles")
nyles.setWeather(weather)
nyles.setResponseObject()

#nyles.greeting()
#nyles.pendingRequestMessage()


def parseAudio(audio): 

	# Speech recognition using Google Speech Recognition
	try:
		said = r.recognize_google_cloud(audio,credentials_json=google)
		return str(said)
	except sr.UnknownValueError:
	    return "I could not understand you"
	except sr.RequestError as e:
	    return "There was a problem with my brain. The problem is "+format(e)



while True:
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)
	
	whatWasSaid = parseAudio(audio)
	nyles.query(whatWasSaid)	   



#nyles.say("The weather is currently "+weather.currentSummary()
#	+" with a temperature of "
#	+str(weather.currentTemperature())
#	+"degrees")

#nyles.say("The daily weather summary is "+weather.dailySummary())




