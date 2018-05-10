import time

import redis
from flask import Flask, make_response, jsonify, request
from j9 import Queue

from maid_tasks.tasks import TASKS


app = Flask(__name__)
queue = Queue()


@app.route('/heartbeat', methods=['GET'])
def heartbeat():
    result = {
        'status': True,
        'message': 'Welcome home, Master!'
    }
    return make_response(jsonify(result))


@app.route('/order', methods=['POST'])
def order():
    action = request.json['action']
    task = TASKS.get(action)
    if task is None:
        response = {
            'status': False,
            'message': 'Task not found',
        }
        return make_response(jsonify(response))
    job_id = queue.enqueue(task)
    response = {
        'status': True,
        'job_id': job_id,
    }
    return make_response(jsonify(response))


@app.route('/result', methods=['POST'])
def result():
    job_id = request.json['job_id']
    r = queue.result.get(job_id)
    if r is None:
        response = {
            'status': False,
            'message': 'No such job_id',
        }
        return make_response(jsonify(response))
    response = {
        'status': True,
        'result': r,
    }
    return make_response(jsonify(response))


if __name__ == '__main__':
    queue.start()
    app.run('0.0.0.0', port=8080, debug=True)
