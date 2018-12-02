import pickle
from flask import Flask
from flask_cors import CORS, cross_origin
from sklearn.naive_bayes import MultinomialNB

app = Flask(__name__)
CORS(app)


def init():
    model = pickle.load(open("trained_nlp.p", "rb"))
    count_vec = pickle.load(open("caount_vec.p", "rb"))

    return model, count_vec


@app.route('/output/<word>', methods=['GET'])
def nlp_result(word):
    model, count_vec = init()
    predict = model.predict(count_vec.transform([str(word)]))[0]
    print(predict)
    return str(predict)


if __name__ == '__main__':
    app.run()
