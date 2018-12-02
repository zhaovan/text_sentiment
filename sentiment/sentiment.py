from textblob import TextBlob
from sys import argv

from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route('/sentiment', methods=['GET'])
def sentiment_analysis(inp):
    text = TextBlob(inp.readline())
    for sentence in text.sentences:
        print(sentence.sentiment)


if __name__ == "__main__":
    f = open(argv[1], "r")
    sentiment_analysis(f)
