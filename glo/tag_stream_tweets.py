# Import data and tagger
import json
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents
import os
cwd = os.getcwd()

data = cwd+'/glo.json'

tweets_tokens = twitter_samples.tokenized(data)

# Tag tagged tweets
tweets_tagged = pos_tag_sents(tweets_tokens)

# print Tag tagged tweets
print(tweets_tagged)
