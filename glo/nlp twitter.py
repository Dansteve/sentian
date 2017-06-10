# Import data and tagger
import json
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents
import os
cwd = os.getcwd()

data = cwd+'\\glo.txt'

# Load tokenized tweets
tweets_tokens = twitter_samples.tokenized(data)

# Tag tagged tweets
tweets_tagged = pos_tag_sents(tweets_tokens)

# Set accumulators
CD_count = 0
AT_count = 0
JJ_count = 0
NN_count = 0
RB_count = 0
NNS_count = 0
VBG_count = 0
VBD_count = 0

# Loop through list of tweets
for tweet in tweets_tagged:
    for pair in tweet:
        tag = pair[1]
        if tag == 'CD':
            CD_count += 1
        elif tag == 'AT':
            AT_count += 1
        elif tag == 'JJ':
            JJ_count += 1
        elif tag == 'NN':
            NN_count += 1
        elif tag == 'RB':
            RB_count += 1
        elif tag == 'NNS':
            NNS_count += 1
        elif tag == 'VBG':
            VBG_count += 1
        elif tag == 'VBD':
            VBD_count += 1

# Print total numbers for each part of speech
print('Total number of cardinal numbers = ', CD_count)
print('Total number of articles = ', AT_count)
print('Total number of adjectives = ', JJ_count)
print('Total number of nouns formed from adjectives = ', NN_count)
print('Total number of adverbs = ', RB_count)
print('Total number of plural nouns = ', NNS_count)
print('Total number of gerunds = ', VBG_count)
print('Total number of past tense verbs = ', VBD_count)