import json
import requests

from utils.CustomExceptions import ResponseStatusCodeException, ResponseErrorException


class ApiClient:

    def __init__(self):
        self.session = requests.Session()
        self.csrf_token = None

    def _request(self, method, location, headers=None, data=None, expected_status=200, jsonify=True):
        url = location

        response = self.session.request(method, url, headers=headers, data=data)

        if response.status_code != expected_status:
            raise ResponseStatusCodeException(f'Got {response.status_code} {response.reason} for URL "{url}"!\n'
                                              f'Expected status_code: {expected_status}.')

        if jsonify:
            json_response = response.json()
            if json_response.get('bStateError'):
                error = json_response.get('bErrorMsg', 'Unknown')
                raise ResponseErrorException(f'Request "{url}" return error "{error}"!')
            return json_response
        return response

    @property
    def post_headers(self):
        return {'X-CSRFToken': self.csrf_token}

    def get_csrf_token(self):

        location = 'https://target.my.com/csrf/'

        headers = self._request('GET', location=location, jsonify=False).headers['set-cookie'].split(';')
        token_header = [h for h in headers if 'csrftoken' in h]
        if not token_header:
            raise Exception('CSRF token not found in main page headers')

        token_header = token_header[0]
        token = token_header.split('=')[-1]
        return token

    def post_login(self, user, password):
        location = 'https://auth-ac.my.com/auth'

        headers = {
            "Referer": "https://account.my.com/",
        }

        data = {
            'email': user,
            'password': password,
            'continue': 'https://target.my.com/',
            'failure': 'https://account.my.com/login/?continue=https%3A%2F%2Faccount.my.com',
        }

        result = self._request('POST', location=location, headers=headers, data=data, jsonify=False)

        self.csrf_token = self.get_csrf_token()

        return result

    def post_segment_create(self, name_segment):
        location = 'https://target.my.com/api/v2/remarketing/segments.json'

        headers = self.post_headers

        data = {
            "name": name_segment, "pass_condition": 1, "relations":
                [
                    {
                        "object_type": "remarketing_player", "params": {"type": "positive", "left": 365, "right": 0}
                    }
                ],
            "logicType": "or"
        }

        result = self._request('POST', location=location, headers=headers, data=json.dumps(data))
        return result

    def post_delete_segment(self, source_id):
        location = 'https://target.my.com/api/v1/remarketing/mass_action/delete.json'
        headers = self.post_headers

        data = [{"source_id": source_id,
                "source_type": "segment"}]

        result = self._request('POST', location=location, headers=headers, data=json.dumps(data))
        return result
