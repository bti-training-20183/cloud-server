from flask import Flask, request
from flask_cors import CORS, cross_origin
import os
import sys
sys.path.append(os.getcwd())


app = Flask(__name__)
app.config.from_pyfile('config.py')
CORS(app)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/upload', methods=["GET", "POST"])
def upload():
    print(request.files)
    return 'Hello'

@app.route('/model/<model_id>', methods=["GET"])
def getModel(model_id):
    return 'model'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')
