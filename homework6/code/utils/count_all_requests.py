import os


def count_all_requests():

    cur_path = os.path.dirname(__file__)
    file_name = 'access.log'
    len_folder = len(cur_path.split('/')[6])
    len_cur_path = len(cur_path)

    with open(cur_path[0:(len_cur_path-len_folder)] + file_name, 'r') as f:
        count_requests = 0
        while f.readline() != "":
            count_requests += 1
        return count_requests



