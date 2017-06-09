# Import data and tagger
from nltk.corpus import twitter_samples

# Load  tweets
tweets = twitter_samples.strings('positive_tweets.json')

# Load tokenized tweets
tweets_tokens = twitter_samples.tokenized('positive_tweets.json')

# print tokens tweets
print(tweets_tokens)
