import config
from utils.message_handler import Message_Handler
from utils.datastore_handler import DataStore_Handler
from utils.database_handler import Database_Handler
from flask import Flask, request, flash, redirect
from flask_cors import CORS, cross_origin
from werkzeug.datastructures import ImmutableMultiDict
import os
import json
import sys
sys.path.append(os.getcwd())
if not os.path.exists('tmp'):
    os.makedirs('tmp')
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
    print(request.form)
    print("___")
    print(request.files.to_dict())
    f = request.files.to_dict()['data']
    filename = f.filename
    from_path = 'tmp/'+filename
    to_path = filename.split('.')[0] + '/raw/' + filename
    f.save(from_path)
    DataStore_Handler.upload(from_path,to_path)
    msg = {
        "name": filename,
        "type": filename.split('.')[1],
        "date": request.form['date'],
        "file_uri": to_path
    }
    Message_Handler.sendMessage('from_client', json.dumps(msg))
    Database_Handler.insert(msg)
    return 'Hello'


@app.route('/model/<model_id>', methods=["GET"])
def getModel(model_id):
    return 'model'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')
