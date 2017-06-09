# Import data and tagger
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents

# Load tokenized tweets
tweets_tokens = twitter_samples.tokenized('positive_tweets.json')

# Tag tagged tweets
tweets_tagged = pos_tag_sents(tweets_tokens)

# print Tag tagged tweets
print(tweets_tagged)
