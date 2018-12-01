from flask import Flask
from flask_cors import CORS, cross_origin

<<<<<<< HEAD
def hello():
    print "Hi"
=======
app = Flask(__name__)
CORS(app)

@app.route('/output', methods=['GET'])
def output():
	return "HELLO IT WORKS"
>>>>>>> 9f1bed5147b26f8efdb3b39716f2de00302b4e92

if __name__ == "__main__":
	app.run()
