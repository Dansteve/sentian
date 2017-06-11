from time import sleep
from selenium import webdriver

class TweetScrapper():
	def __init__(self, url=None,useInfiniteScroll=True,browser="firefox",browserDriverPath="Path/to/driver"):
		self.url = url
		
		# Download Chrome Driver or geckodriver for firefox to use selenium
		# 
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
	scrapper = TweetScrapper(url="https://twitter.com/search?src=typd&q=gloworld%20glocare",browserDriverPath="path/to/driver")
	scrapper.infiniteScroller()
	scrapper.gatherTweetsFromPage(tweetCssClass="tweet-txt")
	scrapper.saveTweets(fileName="tweet.txt")
