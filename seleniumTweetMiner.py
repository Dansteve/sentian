from time import sleep

from selenium import webdriver

url = "https://twitter.com/search?src=typd&q=gloworld%20glocare"

browser = webdriver.Firefox(executable_path='/home/otse/Downloads/geckodriver')
browser.get(url)

for _ in range(2000):
	browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
	sleep(3)

tweets = browser.find_elements_by_class_name("tweet-text")

file = open("tweets.txt","w")

for tweet in tweets:
	file.write("tweet: "+tweet.text+",\n")