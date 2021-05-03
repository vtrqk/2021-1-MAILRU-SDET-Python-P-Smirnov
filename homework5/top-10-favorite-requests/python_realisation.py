import operator
import os
cur_path = os.path.dirname(__file__)
file_name = 'access.log'
len_folder = len(cur_path.split('/')[4])
len_cur_path = len(cur_path)

with open(cur_path[0:(len_cur_path - len_folder)] + file_name, 'r') as f:
    current_string = f.readline()
    unique_url_map: dict = {}
    while current_string != "":
        if unique_url_map.get(current_string.split(' ')[6]) is None:
            unique_url_map[current_string.split(' ')[6]] = 0
        else:
            temp_var = unique_url_map.get(current_string.split(' ')[6]) + 1
            unique_url_map.update({current_string.split(' ')[6]: temp_var})
        current_string = f.readline()

    marklist = sorted(unique_url_map.items(), key=operator.itemgetter(1), reverse=True)
    sortdict = dict(marklist)
    top_number = 0
    for key, value in sortdict.items():
        if(top_number != 10):
            print(f'URL is {key}  |  count of requests {value}')
        else:
            exit()
        top_number += 1