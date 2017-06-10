# Import data and tagger
import json
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents
import os

cwd = os.getcwd()


data = cwd+'\\glo.txt'

# Load  tweets
tweets = twitter_samples.strings(data)

# print tweets
print(tweets)
