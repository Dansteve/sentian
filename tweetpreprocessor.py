import json
import re
import string

from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords
from nltk import pos_tag


class TweetPreprocessor(TweetTokenizer):

	def __init__(self,filepath="glotweets.json"):
		super().__init__(strip_handles=True, reduce_len=True)

		self.filepath = filepath
		self.stopwords = set(stopwords.words("english"))
		self.punctuation = string.punctuation
		self.raw_tweets = []

		self.__loadTweetsFromFile()
		self.__tokenize()
		self.__removeStopwordsAndPunctuations()
		self.__tagTweets()


	def __loadTweetsFromFile(self):
		with open(self.filepath, "r") as tweetfile:
			tweets = json.load(tweetfile)

		number_of_tweets = len(tweets["glo"])
		for i in range(number_of_tweets):
			self.raw_tweets.append(tweets["glo"][i]["tweet"])

	def __tokenize(self):
		self.tokenized_tweets = []
		for tweet in self.raw_tweets:
			self.tokenized_tweets.append(super().tokenize(tweet))
		
		return self.tokenized_tweets

	def __removeStopwordsAndPunctuations(self):
		self.filtered_tweets = []

		#this creates a regex pattern to check if a token is a punctuation or a series of punctuations
		pattern = re.compile("[{0}{1}]+".format(re.escape(self.punctuation),"\s"))

		for tweet in self.tokenized_tweets:
			filtered_tweet = []
			for token in tweet:
				if token not in self.stopwords:
					if pattern.fullmatch(token) == None: # filters punctuations 
						filtered_tweet.append(token)

			self.filtered_tweets.append(filtered_tweet)

		return self.filtered_tweets

	def __tagTweets(self):
		self.tagged_tweets = []

		for tweet in self.filtered_tweets:
			self.tagged_tweets.append(pos_tag(tweet))

		return self.tagged_tweets

