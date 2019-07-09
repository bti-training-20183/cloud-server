import config
from utils.message_handler import MessageHandler
from flask import Flask, request, flash, redirect
from flask_cors import CORS, cross_origin
from werkzeug.datastructures import ImmutableMultiDict
import os
import sys
sys.path.append(os.getcwd())

app = Flask(__name__)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
CORS(app)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/upload', methods=["POST"])
def upload():
    # print(request)
    # print(request.form)
    print(request.files.to_dict())
    f = request.files.to_dict()['data']
    f.save('test.txt')
    # TO DO
    # Save the file to Minio and send file's URL 
    return 'Hello'


@app.route('/model/<model_id>', methods=["GET"])
def getModel(model_id):
    return 'model'


if __name__ == '__main__':
    MessageHdlr = MessageHandler(config.RABBITMQ_CONNECTION)
    app.run(debug=True, host='0.0.0.0', port='8000')
