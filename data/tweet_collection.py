import tweepy
import json
import pandas as pd
import re

# input your credentials here
consumer_key = '0ogC7KrlKH2xaQz92vXFfugO2'
consumer_secret = 'iGo86bEl7ZulPPFj0dWlQMOV9HF1XXOrNvqy4LTnIMeN9hrkK8'
access_token = '1406462390-pzLO8OYgsW9b4zr8nHtQ56MmVnrxSgYKuE8ToZD'
access_token_secret = 'rE6pVJqca8l4VHtl952u7hwr3qtuIPIIcBPj6lhWS0l7W'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
# United Airlines
# Open/Create a file to append data

file_d = 'drunk.json'
file_s = 'sober.json'

csvFile = open(file_d, 'w+')

query = "#wasted"
# queries = ['sober']

count = 0
data = []

res = tweepy.Cursor(api.search, q=query,
                    count=20000,
                    lang="en",
                    show_user="true",
                    since="2017-01-01").items()
for tweet in res:
    url = re.match(
        '(?P<url>https?://[^\s]+)', tweet.text)

    if url:
        continue

    text = " ".join(re.findall("[a-zA-Z]+", tweet.text))
    data.append(text)
    count = count + 1

res = tweepy.Cursor(api.search, q='#drunk',
                    count=20000,
                    lang="en",
                    show_user="true",
                    since="2017-01-01").items()
for tweet in res:
    url = re.match(
        '(?P<url>https?://[^\s]+)', tweet.text)

    if url:
        continue

    text = " ".join(re.findall("[a-zA-Z]+", tweet.text))
    data.append(text)
    count = count + 1


json.dump(data, csvFile)
print(count)
