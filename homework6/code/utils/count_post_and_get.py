import os


def count_post_and_get():
    cur_path = os.path.dirname(__file__)
    file_name = 'resources/access.log'
    len_folder = len(cur_path.split('/')[7])
    len_cur_path = len(cur_path)

    with open(cur_path[0:(len_cur_path - len_folder)] + file_name, 'r') as f:
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
