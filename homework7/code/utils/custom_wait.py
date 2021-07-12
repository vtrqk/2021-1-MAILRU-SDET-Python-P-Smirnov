import time
import requests
from requests.exceptions import ConnectionError


def wait(host, port, err_name):
    started = False
    st = time.time()
    url = f'http://{host}:{port}'
    while time.time() - st < 2:
        try:
            requests.get(url)
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError(f'{err_name} did not started in 5s!')
