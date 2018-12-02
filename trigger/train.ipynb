{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import pandas as pd\n",
    "import os\n",
    "\n",
    "\n",
    "from sklearn.datasets import fetch_20newsgroups\n",
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "from sklearn.feature_extraction.text import TfidfTransformer\n",
    "from sklearn.naive_bayes import MultinomialNB\n",
    "from sklearn.linear_model import SGDClassifier\n",
    "\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "ask = pd.read_csv(\"../data/final_ask.csv\", header=None)\n",
    "ask = ask.iloc[1:].drop_duplicates(subset=[0])\n",
    "college = pd.read_csv(\"../data/college_csv.csv\", header=None).drop_duplicates(subset=[0])\n",
    "combined = pd.read_csv(\"../data/combined_csv.csv\", header=None).drop_duplicates(subset=[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "print(combined)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "support = pd.read_csv(\"../data/support_csv.csv\", header=None).drop_duplicates(subset=[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.concat([ask, college, support, combined])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.sample(frac=1).reset_index(drop=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "ask = pd.DataFrame({0 : ['hello hello my name is', 'a'], 1: [0, 1]})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# print(type(ask.iloc[0,1]))\n",
    "# twenty_test = fetch_20newsgroups(subset='test', shuffle=True)\n",
    "# print(twenty_test.data[0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "count_vect = CountVectorizer(stop_words='english')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "X_train_counts = count_vect.fit_transform(df.iloc[0:400000, 0])\n",
    "# print(X_train_counts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(400000, 160517)\n"
     ]
    }
   ],
   "source": [
    "tfidf_transformer = TfidfTransformer()\n",
    "X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)\n",
    "print(X_train_tfidf.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "ename": "TypeError",
     "evalue": "'SGDClassifier' object is not callable",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-14-6d9d885ffc9b>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[0mclf\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mSGDClassifier\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mloss\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'hinge'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mpenalty\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;34m'l2'\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0malpha\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m1e-3\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mn_iter\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mrandom_state\u001b[0m\u001b[1;33m=\u001b[0m\u001b[1;36m42\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mX_train_tfidf\u001b[0m\u001b[1;33m,\u001b[0m \u001b[0mdf\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0miloc\u001b[0m\u001b[1;33m[\u001b[0m\u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;36m400000\u001b[0m\u001b[1;33m,\u001b[0m \u001b[1;36m1\u001b[0m\u001b[1;33m]\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m: 'SGDClassifier' object is not callable"
     ]
    }
   ],
   "source": [
    "clf = MultinomialNB().fit(X_train_tfidf, df.iloc[0:400000, 1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 0 1 ... 1 1 0]\n"
     ]
    }
   ],
   "source": [
    "predicted = clf.predict(count_vect.transform(df.iloc[400001:, 0]))\n",
    "print(predicted)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8302772158907143"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "np.mean(predicted == df.iloc[400001:, 1])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
