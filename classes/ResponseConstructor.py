import re
import random
import json
from functions.functions import openApp
from difflib import SequenceMatcher

class ResponseConstructor:

	def __init__(self,weather,master):
		self.weather 	= weather
		self.master		= master
		self.responses 	= json.loads(open('data/responses.json').read())
		#print(self.responses)


	def checkKeyValuePairExistence(self, dic, key):
		try:
			return dic[key]
		except KeyError:
			return False

	def similar(self,a, b):
		return SequenceMatcher(None, a, b).ratio()		

	def compareQuestionToAllKnownQuestions(self,quesiton):
		print("Using comparison method")
		print(self.responses["queries"].keys())
		for possibleQuestion in self.responses["queries"].keys():
			print(self.similar(possibleQuestion,quesiton))
			if self.similar(possibleQuestion,quesiton) > 0.5:
				print(possibleQuestion)
				return self.responses["queries"][possibleQuestion]
		return False

	def isStoreInfo(self,question):
		response = False
		if "my name is" in question:
			response = re.sub('my name is', "", question)
			self.master = response
			response = "Hello, "+response
		return response

	def isOpenAppCommand(self,question):
		response = False
		if "open" in question:
			response = re.sub('open',"",question)
			response = openApp(response)
			return response
		else:
			return response


	def getResponseToQuestion(self,question):
		storeInfoCheck 	= self.isStoreInfo(question)
		if storeInfoCheck != False:
			return storeInfoCheck

		appCheck 		= self.isOpenAppCommand(question)
		if appCheck != False:
			return appCheck

		if self.checkKeyValuePairExistence(self.responses["queries"],question) != False:
			return self.buildResponse(self.responses["queries"][question])

		responseType = self.compareQuestionToAllKnownQuestions(question)
		if responseType != False:
			return self.buildResponse(responseType)	
		else:
			return "I'm sorry, I don't understand what you mean by "+question

	def buildResponse(self, responseType,context = None):
		response = self.responses["responses"][responseType]
		response = random.choice(response)
		#print(response)
		if responseType == "weather data":
			response = response + self.weather.currentSummary() + " and the current temperature is " +str(self.weather.currentTemperature()) + " degrees"
		elif responseType == "master name":
			response = re.sub('(master)', self.master, response)
		return response	
