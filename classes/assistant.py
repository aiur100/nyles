from subprocess import call

class Assistant:
	def __init__(self,name,master = "master"):
		self.name 	= name
		self.master = master 

	def greeting(self):
		self.say("Hello "+self.master+", My name is "+self.name)

	def pendingRequestMessage(self):
		self.say("How can I be of service?")		

	def say(self,message):
		call(["say", message])
