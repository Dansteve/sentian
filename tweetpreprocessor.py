import json
import re
import string

from nltk.tokenize import TweetTokenizer
from nltk.corpus import stopwords


class TweetPreprocessor(TweetTokenizer):

	def __init__(self,filepath="glotweets.json"):
		super().__init__(strip_handles=True, reduce_len=True)

		self.filepath = filepath
		self.stopwords = set(stopwords.words("english"))
		self.punctuation = string.punctuation
		self.raw_tweets = []

		self.__loadTweetsFromFile()


	def __loadTweetsFromFile(self):
		with open(self.filepath, "r") as tweetfile:
			tweets = json.load(tweetfile)

		number_of_tweets = len(tweets["glo"])
		for i in range(number_of_tweets):
			self.raw_tweets.append(tweets["glo"][i]["tweet"])

	def tokenize(self):
		self.tokenized_tweets = []
		for tweet in self.raw_tweets:
			self.tokenized_tweets.append(super().tokenize(tweet))
		
		#return self.tokenized_tweets

	def removeStopwordsAndPunctuations(self):
		self.filtered_tweets = []
		pattern = re.compile("[{0}{1}]+".format(re.escape(self.punctuation),"\s"))

		for tweet in self.tokenized_tweets:
			filtered_tweet = []
			for token in tweet:
				if token not in self.stopwords:
					if pattern.fullmatch(token) == None:
						filtered_tweet.append(token)

			self.filtered_tweets.append(filtered_tweet)


if __name__ == '__main__':
	tp = TweetPreprocessor()
	tp.tokenize()
	tp.removeStopwordsAndPunctuations()
	print(tp.filtered_tweets)