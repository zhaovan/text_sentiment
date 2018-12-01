from textblob import TextBlob
from sys import argv

def sentiment_analysis(inp):
    text = TextBlob(inp.readline())
    for sentence in text.sentences:
        print(sentence.sentiment)

if __name__ == "__main__":
    f = open(argv[1], "r")
    sentiment_analysis(f)