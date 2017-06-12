from nltk.tokenize import TweetTokenizer
import json
import re

<<<<<<< HEAD
class TweetPreprocessor(TweetTokenizer):
=======
class TweetPreprocessor():
>>>>>>> 7a626168d76eaf1d1fe00e7a05171e23e6f7d4aa
	def __init__(self,filepath="glotweets.json"):
		super().__init__(strip_handles=True, reduce_len=True)
		self.filepath = filepath

		with open(self.filepath, "r") as tweetfile:
			self.tweets = json.load(tweetfile)

<<<<<<< HEAD
	def tokenize(self,text):
		return super().tokenize(text)

=======
>>>>>>> 7a626168d76eaf1d1fe00e7a05171e23e6f7d4aa
