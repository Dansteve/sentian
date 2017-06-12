from nltk.tokenize import TweetTokenizer
import json
import re

class TweetPreprocessor(TweetTokenizer):
	def __init__(self,filepath="glotweets.json"):
		super().__init__(strip_handles=True, reduce_len=True)
		self.filepath = filepath

		with open(self.filepath, "r") as tweetfile:
			self.tweets = json.load(tweetfile)

	def tokenize(self,text):
		return super().tokenize(text)

