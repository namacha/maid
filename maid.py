import time

import redis
from flask import Flask, make_response, jsonify, request
from queue import Queue


app = Flask(__name__)
queue = Queue()


@api.route('/heartbeat', methods=['GET'])
def heartbeat():
    result = {
        'result': True,
        'message': 'Welcome home, Master!'
    }
    return make_response(jsonify(result))


@app.route('/order', methods=['POST'])
def order():
    action = request.json['action']
    job_id = queue.enqueue
