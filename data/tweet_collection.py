import tweepy
import csv
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

file_d = 'drunk.csv'
file_s = 'sober.csv'

csvFile = open(file_d, 'a+')

# Use csv Writer
csvWriter = csv.writer(csvFile)

query = "#wasted"
# queries = ['sober']

count = 0


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

    csvWriter.writerow([str(tweet.created_at), tweet.text.encode(
        'utf-8'), tweet.user.screen_name.encode('utf-8')])
    print(count)
    count = count + 1

print(count)
