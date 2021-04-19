import requests
from requests.cookies import cookiejar_from_dict


class ApiClient:

    def __init__(self):
        self.session = requests.Session()
        self.csrf_token = None

    def get_csrf_token(self):
        location = 'https://target.my.com/csrf/'
        headers = self.session.get(location).headers['set-cookie'].split(';')
        token_header = [h for h in headers if 'csrftoken' in h]
        if not token_header:
            raise Exception('CSRF token not found in main page headers')

        token_header = token_header[0]
        token = token_header.split('=')[-1]
        print(token)
        self.csrf_token = token

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

        result = self.session.post(location, headers=headers, data=data)
        mc_token = self.session.cookies['mc']
        sdcs_token = self.session.cookies['sdcs']

        self.session.cookies = cookiejar_from_dict({'mc': mc_token, 'sdcs': sdcs_token})
        return result

    def post_segment_create(self, name_segment):
        location = 'https://target.my.com/api/v2/remarketing/segments.json'
        headers = {
            'Content-Type': 'aapplication/json',
            'Cookie': f'csrftoken={self.csrf_token}',
        }
        data = {
            'name': f'{name_segment}',
            'pass_condition': '2',
            'relations': [
                {
                    "object_type": "remarketing_counter",
                    "params": {
                        "goal_id": "uss", "right": "0", "type": "positive", "counter_id": "2500001", "left": "365"
                    }
                },
                {
                    "object_type": "segment",
                    "object_id": '1166'
                }
            ]
        }
        result = self.session.post(location, headers=headers, data=data)
        return result.json()

    def post_delete_segment(self, source_id):
        location = 'https://target.my.com/api/v1/remarketing/mass_action/delete.json'
        headers = {
            'Content-Type': 'aapplication/json',
            'Cookie': f'csrftoken={self.csrf_token}',
        }
        data = {
            "errors": [],
            "successes": [
                {
                    "source_id": source_id, "source_type": "segment"
                }
            ]

        }
        result = self.session.post(location, headers=headers, data=data).json()
        assert (result['successes']['source_id']) == source_id
