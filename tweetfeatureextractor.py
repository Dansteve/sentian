from tweetpreprocessor import TweetPreprocessor
from sklearn.feature_extraction import DictVectorizer


class FeatureExtractor(DictVectorizer):

	def __init__(self):
		super().__init__()
		self._tp = TweetPreprocessor()
		self.tagged_tweets = self._tp.tagged_tweets

	def pos_vectorizer(self):
		self.featureExtract = super().fit_transform(self.tagged_tweets)
		return self.featureExtract

if __name__ == '__main__':
    fe = FeatureExtractor(tt)
    pro = fe.pos_vectorizer()
    print(pro)
    
