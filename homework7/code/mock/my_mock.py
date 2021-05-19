import threading

from flask import Flask, jsonify, request

import settings

app = Flask(__name__)

JOB_DATA = {}


@app.route('/get_job/<name>', methods=['GET'])
def get_user_job(name):
    if job := JOB_DATA.get(name):
        return jsonify(job), 200
    else:
        return jsonify(f'Job for user {job} not fount'), 404


@app.route('/update_job/<name>', methods=['PUT'])
def put_user_job(name):
    if JOB_DATA.get(name):
        JOB_DATA[name] = request.json('job')
        return jsonify(JOB_DATA[name]), 200
    else:
        return jsonify(f'Job for user {name} not fount'), 404


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MY_MOCK_HOST,
        'port': settings.MY_MOCK_PORT
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