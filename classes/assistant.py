from subprocess import call
from classes.ResponseConstructor	import ResponseConstructor
import random
import json
import re

class Assistant:
	greetings = ["hello!","howdy","What's up?","hola!","bonjour","hi there","shalom alone, my friend","hey, what's uup!"]
	howAreYou = ["I'm the best there is","I'm pretty good"]

	def __init__(self,name,master = "master"):
		self.name 	= name
		self.master = master

	def setWeather(self,weatherObject):
		self.weather = weatherObject

	def setResponseObject(self):
		self.ResponseConstructor = ResponseConstructor(self.weather,self.master)	

	def greeting(self):
		self.say("Hello "+self.master+", My name is "+self.name)

	def pendingRequestMessage(self):
		self.say("How can I be of service?")		

	def say(self,message):
		call(["say", message])	

	def query(self,question):
		if("computer" not in question):
			return
		question = re.sub('(computer)', '', question)	
		question = question.strip()
		question = question.lower()
		print(question)
		response = self.ResponseConstructor.getResponseToQuestion(question)
		self.say(response)
			
						
