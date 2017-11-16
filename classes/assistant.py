from subprocess import call
import random

class Assistant:
	greetings = ["hello!","howdy","What's up?","hola!","bonjour","hi there","shalom alone, my friend","hey, what's uup!"]
	howAreYou = ["I'm the best there is","I'm pretty good"]

	def __init__(self,name,master = "master"):
		self.name 	= name
		self.master = master

	def setWeather(self,weatherObject):
		self.weather = weatherObject

	def greeting(self):
		self.say("Hello "+self.master+", My name is "+self.name)

	def pendingRequestMessage(self):
		self.say("How can I be of service?")		

	def say(self,message):
		call(["say", message])

	def query(self,question):
		if "hello" in question:
			self.say(random.choice(self.greetings))
		elif "hi" in question:
			self.say(random.choice(self.greetings))	
		elif "how are you" in question:
			self.say("I'm always well, thank you!")
		elif "I could not understand you" in question:
			print("nothing to say")
		elif "weather" in question:
			 self.say("The weather is currently "+self.weather.currentSummary())
			 self.say("Temperature seems to be about "+self.weather.currentTemperature()+" degrees")	
		else:
			self.say("oh, wow, I am not really sure what you mean by, "+question+". My master just made me, so I am learning slowly")	
						
