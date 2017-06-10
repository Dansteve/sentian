# Import data and tagger
import json
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents
import os
cwd = os.getcwd()

data = cwd+'\\glo.txt'

# Load tokenized tweets
tweets_tokens = twitter_samples.tokenized(data)

# print tokens tweets
print(tweets_tokens)
