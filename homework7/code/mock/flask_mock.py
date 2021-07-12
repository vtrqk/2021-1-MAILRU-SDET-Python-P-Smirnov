import threading
import settings

from flask import Flask, jsonify, request

app = Flask(__name__)

SURNAME_DATA = {}


@app.route('/get_surname/<name>', methods=['GET'])
def get_user_surname(name):
    if surname := SURNAME_DATA.get(name):
        return jsonify(surname), 200
    else:
        return jsonify(f'Surname for user {name} not fount'), 404


@app.route('/update_surname/<name>', methods=['PUT'])
def put_user_surname(name):
    if SURNAME_DATA.get(name):
        post_data = request.get_json()
        SURNAME_DATA[name] = post_data['surname']
        return jsonify(SURNAME_DATA[name]), 200

    else:
        return jsonify(f'Surname for user {name} not fount'), 404


@app.route('/delete_surname/<name>', methods=['DELETE'])
def delete_user_surname(name):
    if SURNAME_DATA.get(name):
        return jsonify(SURNAME_DATA.pop(name)), 200

    else:
        return jsonify(f'Surname for user {name} not fount'), 404


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'OK, exiting'), 200

