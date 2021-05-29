import os


def count_post_and_get():

    file_access_path = 'resources/access.log'

    with open(os.path.join(os.path.dirname(os.getcwd()), file_access_path), 'r') as f:
        count_get_requests: int = 0
        count_post_requests: int = 0
        current_string: str = f.readline()
        while current_string != "":
            if current_string.find('POST') != -1:
                count_post_requests += 1
            elif current_string.find('GET') != -1:
                count_get_requests += 1
            current_string = f.readline()

        return count_get_requests, count_post_requests
