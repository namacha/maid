# -*- coding: utf-8 -*-

from flask import Flask, jsonify, abort, make_response, request


api = Flask(__name__)


@api.route('/api/greet', methods=['GET'])
def heartbeat():
    result = {
        'result': True,
        'message': 'Welcome home, Master!'
    }
    return make_response(jsonify(result))


@api.route('/api/order', methods=['POST'])
def order():
    print(request.json)
    return jsonify(res='ok')


if __name__ == '__main__':
    api.run('0.0.0.0', port=3000, debug=True)
