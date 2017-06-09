# Import data and tagger
from nltk.corpus import twitter_samples

# Load  tweets
tweets = twitter_samples.strings('positive_tweets.json')

# print tweets
print(tweets)
