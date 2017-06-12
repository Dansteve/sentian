import re

from urllib import parse
from time import sleep
from selenium import webdriver

# Download Chrome Driver or geckodriver for firefox to use selenium
# and use the file path as the browserDriverPath parameter value.

class TweetScrapper(object):
	def __init__(self,url= "https://twitter.com/search?", query=None, tweetCssClass="tweet-text",
				useInfiniteScroll=True,
		     	browser="firefox",browserDriverPath=None):
		
		self.query = query or ""
		query_dict = {"q":self.query}
		encoded_query = parse.urlencode(query_dict)
		
		self.url = url + encoded_query
		self.tweetCssClass = tweetCssClass
		
		if browserDriverPath != None:
			self.browser = webdriver.Firefox(executable_path=browserDriverPath) \
					if browser=="firefox" else webdriver.Chrome(executable_path=browerDriverPath)
		else:
			self.browser = webdriver.Firefox() if browser=="firefox" else webdriver.Chrome()

		self.useInfiniteScroll = useInfiniteScroll

		self.browser.get(self.url)

	def infiniteScroller(self,numberOfScrolls=2000,seconds=3):
		if self.useInfiniteScroll:
			for _ in range(numberOfScrolls):
				self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
				sleep(seconds)
		else:
			print("infinite Scroll disabled on this instance")

	def getTweetsFromPage(self):
		tweets = self.browser.find_elements_by_class_name(self.tweetCssClass)

		return tweets


	def saveTweetsAsJson(self,fileName="glotweets.json"):

		tweets = self.getTweetsFromPage()

		file = open(str(fileName),"w")

		file.write("{\"glo\":[")

		for tweet in tweets:
			tweet_text = re.sub(r"\s\s+"," ",tweet.text)
			tweet_text = tweet_text.replace("\"","\'").replace("\n"," ").replace("\r"," ")
			file.write("{\"tweet\":\""+tweet_text+"\"},")

		file.write("]}")
		file.close()



if __name__ == '__main__':
	# IMPORTANT: Download chromedriver(Google Chrome) or geckodriver(Firefox) to use selenium
	# 	     and use the file path of the driver as the browserDriverPath parameter value.
	scrapper = TweetScrapper(query="gloworld glocare", browserDriverPath="/home/otse/Downloads/geckodriver")
	
	scrapper.infiniteScroller()
	scrapper.saveTweetsAsJson(fileName="glotweets.json")
