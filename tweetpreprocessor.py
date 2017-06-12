import json
import re

from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords


class TweetPreprocessor(TweetTokenizer):

	def __init__(self,filepath="glotweets.json"):
		super().__init__(strip_handles=True, reduce_len=True)

		self.filepath = filepath
		self.stopword_list = stopwords.words("english")
		self.list_of_tweets = []

		self.__loadTweetsFromFile()


	def __loadTweetsFromFile(self):
		with open(self.filepath, "r") as tweetfile:
			tweets = json.load(tweetfile)

		number_of_tweets = len(tweets["glo"])
		for i in range(number_of_tweets):
			self.list_of_tweets.append(tweets["glo"][i]["tweet"])

	def tokenize(self,text):
		return super().tokenize(text)

	def removeStopWords(self):
		pass
