# -*- coding: utf-8 -*-

from flask import Flask, jsonify, abort, make_response


api = Flask(__name__)


@api.route('/greet', methods=['GET'])
def heartbeat():
    result = {
        'result': True,
        'message': 'Welcome home, Master!'
    }
    return make_response(jsonify(result))


if __name__ == '__main__':
    api.run('0.0.0.0', port=3000, debug=True)
