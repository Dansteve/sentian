from urllib import parse
from time import sleep
from selenium import webdriver
import re

# Download Chrome Driver or geckodriver for firefox to use selenium
# and use the file path as the browserDriverPath parameter value.

class TweetScrapper():
	def __init__(self,url= "https://twitter.com/search?", query=None, useInfiniteScroll=True,
		     browser="firefox",browserDriverPath="Path/to/driver"):
		
		self.query = query or ""
		query_dict = {"q":self.query}
		encoded_query = parse.urlencode(query_dict)
		
		self.url = url + encoded_query
		
		self.browser = webdriver.Firefox(executable_path=browserDriverPath) \
				if browser=="firefox" else webdriver.Chrome(executable_path=browerDriverPath)
		self.useInfiniteScroll = useInfiniteScroll

		self.browser.get(self.url)

	def infiniteScroller(self,numberOfScrolls=2000,seconds=3):
		if self.useInfiniteScroll:
			for _ in range(numberOfScrolls):
				self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
				sleep(seconds)
		else:
			print("infinite Scroll disabled on this instance")

	def gatherTweetsFromPage(self,tweetCssClass=None):
		self.tweets = self.browser.find_elements_by_class_name(str(tweetCssClass))


	def saveTweetsAsJson(self,fileName=None):
		file = open(str(fileName),"w")

		file.write("{\"glo\":[")

		for tweet in self.tweets:
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
	scrapper.gatherTweetsFromPage(tweetCssClass="tweet-text")
	scrapper.saveTweetsAsJson(fileName="glotweets.json")
