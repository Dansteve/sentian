import nltk
import json
import re

class TweetPreprocessor():
	def __init__(self,filepath="glotweets.json"):
		self.filepath = filepath

		with open("filepath", "r") as tweetfile:
			self.tweets = json.load(tweetfile)

