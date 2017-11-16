# Nyles - An Assistant for The More Tech-Savy User

**Author:** Christopher R. Hill 
**Contact:** chrishill9 [ AT ] gmail [ the dot ] com

## Overview 
This is just a fun experiment with creating an assistant that would run on 
MacOS machines that will leverage the power of google and other apis to answer
questions like "What's the weather like today?" and "What's the weather for the rest of the week?".

I'd like to support commands that create events, read emails and other content, along with 
search for twitter updates for usernames. 

## Requirements 
* MacOS
* Python 3.6

## Set-up
* You'll need a DarkSky API Key - https://darksky.net
	- In the `keys` directory, there is a file called api_keys.json.  You'll need to update this
	   to include your DarkSky API Key. 
	- Additionally, this uses Google Cloud Speech API, in order to have that working, you will need to put your 
		Google Cloud Speech API generated credentials JSON file in the ```keys/my-google-cloud-speech-credentials.json```.  
		That file doesn't exist, but you will need to create it and put the credentials generated.  
		**FOLLOW THE GETTING STARTED INSTRUCTIONS, SETUP A PROJECT, AND SAVE THAT JSON FILE AS THE FILE NAME LISTED IN THIS README**    


