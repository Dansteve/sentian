from tweetpreprocessor import TweetPreprocessor
from sklearn.feature_extraction import DictVectorizer


class FeatureExtractor(DictVectorizer):

	def __init__(self,tagged_tweets):
		super().__init__()
		self.tagged_tweets = tagged_tweets

	def pos_vectorizer(self):
		self.featureExtract = super().fit_transform(self.tagged_tweets)
		return self.featureExtract

if __name__ == '__main__':
    tp = TweetPreprocessor()
    tt = tp.tagged_tweets
    fe = FeatureExtractor(tt)
    pro = fe.pos_vectorizer()
    print(pro)
    
