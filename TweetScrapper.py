from urllib import parse
from time import sleep
from selenium import webdriver

# Download Chrome Driver or geckodriver for firefox to use selenium
# and use the file path as the browserDriverPath parameter value.

class TweetScrapper():
	def __init__(self,url= "https://twitter.com/search?", query=None, useInfiniteScroll=True,
		     browser="firefox",browserDriverPath="Path/to/driver"):
		
		self.query = query or ""
		query_dict = {"q":self.query}
		encoded_query = parse.urlencode(query_dict)
		
		self.url = url + encoded_query
		
		self.browser = webdriver.FireFox(executable_path=browserDriverPath) \
				if browser=="firefox" else webdriver.Chrome(executable_path=browerDriverPath)
		self.useInfiniteScroll = useInfiniteScroll

		self.browser.get(self.url)

	def infiniteScroller(self,scrollNO=2000,seconds=3):
		if self.useInfiniteScroll:
			for _ in range(scrollNo):
				self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
				sleep(seconds)
		else:
			print("infinite Scroll disabled on this instance")

	def gatherTweetsFromPage(self,tweetCssClass=None):
		self.tweets = self.browser.find_elements_by_class_name(str(tweetCssClass))


	def saveTweets(self,fileName=None):
		file = open(str(fileName),"w")

		for tweet in self.tweets:
			file.write("[tweet: "+tweet.text+"],\n")

if __name__ == '__main__':
	scrapper = TweetScrapper(query="gloworld glocare", browserDriverPath="path/to/driver")
	scrapper.infiniteScroller()
	scrapper.gatherTweetsFromPage(tweetCssClass="tweet-txt")
	scrapper.saveTweets(fileName="tweet.txt")
