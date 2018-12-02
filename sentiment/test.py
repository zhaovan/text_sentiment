from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/output', methods=['GET'])
def output():
	return "HELLO IT WORKS"

if __name__ == "__main__":
	app.run()
