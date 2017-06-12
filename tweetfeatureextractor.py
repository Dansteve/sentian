from tweetpreprocessor import TweetPreprocessor
from sklearn.feature_extraction import DictVectorizer


class featureExtraction(DictVectorizer):

	def __init__(self,tag_tp):
		self.tag_tweets = tag_tp

	def pos_vectorized(self):
    self.vec = DictVectorizer()
		self.featureExtract = self.vec.fit_transform(self.tag_tweets)
		return self.self.featureExtract

if __name__ == '__main__':
    tp = TweetPreprocessor()
	  tp.tokenize()
	  tp.removeStopwordsAndPunctuations()
    tag_tp = tp.tagged_tweets
    fE = featureExtraction()
    pro = fE.pos_vectorized(tag_tp)
    print(pro)
    
