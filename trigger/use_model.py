import pickle
# from sklearn.datasets import fetch_20newsgroups
# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
# from sklearn.linear_model import SGDClassifier

model

def init ():
	model = pickle.load(open( "trained_nlp.p", "rb" ))	

def nlp_result (input):
	return model.predict (input)

