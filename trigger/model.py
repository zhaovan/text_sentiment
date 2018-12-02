
#%%
import json
import pandas as pd
import os


from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier

import numpy as np


#%%
ask = pd.read_csv("../data/final_ask.csv", header=None)
ask = ask.iloc[1:].drop_duplicates(subset=[0])
college = pd.read_csv("../data/college_csv.csv", header=None).drop_duplicates(subset=[0])
combined = pd.read_csv("../data/combined_csv.csv", header=None).drop_duplicates(subset=[0])
support = pd.read_csv("../data/support_csv.csv", header=None).drop_duplicates(subset=[0])

#%%
df = pd.concat([ask, college, support[:200000], combined])

#%%
df = df.sample(frac=1).reset_index(drop=True)


#%%
count_vect = CountVectorizer(stop_words='english')


#%%
X_train_counts = count_vect.fit_transform(df.iloc[0:300000, 0])

#%%
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

#%%
clf = MultinomialNB().fit(X_train_tfidf, df.iloc[0:300000, 1])

#%%
predicted = clf.predict(count_vect.transform(df.iloc[300001:, 0]))

#%%
np.mean(predicted == df.iloc[300001:, 1])



