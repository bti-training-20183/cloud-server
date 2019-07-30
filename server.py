import config
from utils.message_handler import MessageHandler
from utils.datastore_handler import Minio_Handler, S3_Handler
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


@app.route('/create', methods=["POST"])
def create():
    # print(request)
    print(request.form)
    print("___")
    print(request.files.to_dict())
    f = request.files.to_dict()['data']
    fullname = f.filename
    filename, file_extension = os.path.splitext(fullname)
    from_path = 'tmp/' + fullname
    to_path = filename + '/raw/' + filename + file_extension
    f.save(from_path)
    Minio_Handler.upload(from_path, to_path)
    os.remove(from_path)
    msg = {
        "name": filename,
        "type": file_extension,
        "job": 'create',
        "date": request.form['date'],
        "file_uri": to_path
    }
    Message_Handler = MessageHandler(config.RABBITMQ_CONNECTION)
    Message_Handler.sendMessage('from_client', json.dumps(msg))
    Message_Handler.close()
    Database_Handler.insert(msg)
    return 'Hello'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')
