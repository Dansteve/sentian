import json
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents
import os

cwd = os.getcwd()


data = cwd+'\\glo.txt'

# Load  tweets
tweets = twitter_samples.strings(data)


#write to file glo.txt
for tweet in tweets:
    try:
        json1 = json.dumps(tweet, ensure_ascii=False)
    
        with open('m.txt', 'a+') as outfile:
            outfile.write(json.dumps(tweet)+ '\n')
            
    except:
        # read in a line is not in JSON format (sometimes error occured)
        print ("read in a line is not in JSON format (sometimes error occured)")
        continue
