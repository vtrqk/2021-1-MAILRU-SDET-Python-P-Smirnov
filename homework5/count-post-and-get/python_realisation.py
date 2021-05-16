import os

cur_path = os.path.dirname(__file__)
file_name = '/access.log'
len_folder = len(cur_path.split('/')[5])
len_cur_path = len(cur_path)

with open(cur_path[0:(len_cur_path - len_folder)] + file_name, 'r') as f:
    count_get_requests: int = 0
    count_post_requests: int = 0
    current_string: str = f.readline()
    while current_string != "":
        if current_string.split(' ')[5][1:] == "POST":
            count_post_requests += 1
        elif current_string.split(' ')[5][1:] == "GET":
            count_get_requests += 1
        current_string = f.readline()
    print(f'GET - {count_get_requests}, POST - {count_post_requests}')
