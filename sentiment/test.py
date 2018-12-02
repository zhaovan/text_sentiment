from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/output/<word>', methods=['GET'])
def output(word):
	return "HELLO " + word

if __name__ == "__main__":
	app.run()
