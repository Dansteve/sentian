from tweetpreprocessor import TweetPreprocessor
from sklearn.feature_extraction import DictVectorizer


class featureExtractor(DictVectorizer):

	def __init__(self,tagged_tweets):
		super().__init__()
		self.tagged_tweets = tagged_tweets

	def pos_vectorized(self):
		self.featureExtract = super().fit_transform(self.tagged_tweets)
		return self.featureExtract

if __name__ == '__main__':
    tp = TweetPreprocessor()
    tagged_tweets = tp.tagged_tweets
    fe = featureExtractor(tagged_tweet)
    pro = fe.pos_vectorized()
    print(pro)
    
