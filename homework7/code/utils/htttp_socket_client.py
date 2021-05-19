import socket
import json
import settings


class Client:
    def __init__(self):
        self.host = settings.APP_HOST
        self.port = int(settings.APP_PORT)

    def _connection(self):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client.settimeout(0.1)

        client.connect((self.host, self.port))

        return client

    def do_get(self, url, param):

        client = self._connection()

        params = f'{url}{param}'
        request = f'GET {params} HTTP/1.1\r\nHost:{self.host}\r\n\r\n'

        client.send(request.encode())

        total_data = []

        while True:
            data = client.recv(4096)
            if data:
                total_data.append(data.decode())
            else:
                client.close()
                break

        data = ''.join(total_data).splitlines()

        return data

    def do_post(self, url, data):

        client = self._connection()
        json_data = json.dumps(data)

        request = f"POST {url} HTTP/1.1\r\n" \
                  f"Host: {self.host}\r\n" \
                  f"Content-Type: application/json\r\n" \
                  f"Content-Length: " + str(len(json_data)) + "\r\n\r\n" \
                  f"{json_data}"
        client.send(request.encode())

        total_data = []

        while True:
            data_resp = client.recv(4096)
            if data_resp:
                total_data.append(data_resp.decode())
            else:
                client.close()
                break

        data_output = ''.join(total_data).splitlines()

        return data_output
