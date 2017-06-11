import nltk
import json
import re

class TweetPreprocessor():
<<<<<<< HEAD:TweetPreprocessor.py
	def __init__(self,filepath="glotweets.json"):
		self.filepath = filepath

		with open("filepath", "r") as tweetfile:
			self.tweets = json.load(tweetfile)

=======
	def __init__(self):
>>>>>>> aba0be816f9ca164443a0ab6caae0e74ee8bc92d:tweetpreprocessor.py
		
