#import twitter api and system api
import twitter
import sys
import json

#login api
api = twitter.Api(consumer_key='mTjYFcfaSEEpRc8wvq23MYgdV', consumer_secret='IC7q2Uz3p1Uo2VpzsEQJMJg9CKwPCKv90FgVgvoesSC21SU17B', access_token_key='1140329298-qqaNc2XCYTpW6JRjYdT4XBIDDim1G3HbP0ewEMY',access_token_secret='rGr9pSVz8krjWlp4eZKBrI3nw38htSrlsN2eML9zxXVAq')
   
#stream #gloworld tweet
glostream = api.GetStreamFilter(track="glocare")


#write to file glo.txt
for tweet in glostream:
    try:
         
        with open('glo.json', 'a+') as outfile:
            outfile.write(json.dumps(tweet)+ '\n')
            
    except:
        # read in a line is not in JSON format (sometimes error occured)
        print ("read in a line is not in JSON format (sometimes error occured)")
        continue
