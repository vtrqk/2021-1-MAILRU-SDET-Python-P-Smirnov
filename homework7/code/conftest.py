import os
import signal
import subprocess
import sys
import requests
import settings
from copy import copy

from utils.custom_wait import wait
from utils.fixtures import *

repo_root = os.path.abspath(os.path.join(__file__, os.pardir))  # code


def start_app(config):
    app_path = os.path.join(repo_root, 'app', 'app.py')

    app_out = open('/tmp/app_stdout.log', 'w')
    app_err = open('/tmp/app_stderr.log', 'w')

    env = copy(os.environ)
    env['APP_HOST'] = settings.APP_HOST
    env['APP_PORT'] = settings.APP_PORT

    env['STUB_HOST'] = settings.STUB_HOST
    env['STUB_PORT'] = settings.STUB_PORT

    env['MOCK_HOST'] = settings.MOCK_HOST
    env['MOCK_PORT'] = settings.MOCK_PORT

    env['MY_MOCK_HOST'] = settings.MY_MOCK_HOST
    env['MY_MOCK_PORT'] = settings.MY_MOCK_PORT

    proc = subprocess.Popen([sys.executable, app_path], stdout=app_out, stderr=app_err, env=env)

    config.app_proc = proc
    config.app_out = app_out
    config.app_err = app_err

    wait(host=settings.APP_HOST, port=settings.APP_PORT, err_name='App')


def start_stub(config):
    stub_path = os.path.join(repo_root, 'stub', 'flask_stub.py')

    stub_out = open('/tmp/stub_stdout.log', 'w')
    stub_err = open('/tmp/stub_stderr.log', 'w')

    env = copy(os.environ)

    env['STUB_HOST'] = settings.STUB_HOST
    env['STUB_PORT'] = settings.STUB_PORT

    env['MOCK_HOST'] = settings.MOCK_HOST
    env['MOCK_PORT'] = settings.MOCK_PORT
    env['MY_MOCK_HOST'] = settings.MY_MOCK_HOST
    env['MY_MOCK_PORT'] = settings.MY_MOCK_PORT

    proc = subprocess.Popen([sys.executable, stub_path], stdout=stub_out, stderr=stub_err, env=env)

    config.stub_proc = proc
    config.stub_out = stub_out
    config.stub_err = stub_err
    wait(host=settings.STUB_HOST, port=settings.STUB_PORT, err_name='Stub')


def start_mock():
    from mock import flask_mock
    flask_mock.run_mock()
    wait(host=settings.MOCK_HOST, port=settings.MOCK_PORT, err_name='Mock')


def start_my_mock():
    from mock import my_mock
    my_mock.run_mock()
    wait(host=settings.MY_MOCK_HOST, port=settings.MY_MOCK_PORT, err_name='My Mock')


def pytest_configure(config):
    if not hasattr(config, 'workerinput'):
        start_mock()
        start_my_mock()
        start_stub(config)
        start_app(config)


def stop_app(config):
    config.app_proc.send_signal(signal.SIGINT)
    exit_code = config.app_proc.wait()

    config.app_out.close()
    config.app_err.close()

    assert exit_code == 0


def stop_stub(config):
    config.stub_proc.send_signal(signal.SIGINT)
    config.stub_proc.wait()

    config.stub_out.close()
    config.stub_err.close()


def stop_mock(url_shutdown):
    requests.get(url_shutdown)


def pytest_unconfigure(config):
    if not hasattr(config, 'workerinput'):
        stop_app(config)
        stop_stub(config)
        stop_mock(url_shutdown=f'http://{settings.MOCK_HOST}:{settings.MOCK_PORT}/shutdown')
        stop_mock(url_shutdown=f'http://{settings.MY_MOCK_HOST}:{settings.MY_MOCK_PORT}/shutdown')
