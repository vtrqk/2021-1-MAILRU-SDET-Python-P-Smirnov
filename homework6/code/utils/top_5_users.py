import operator
import os


def get_top_users():

    cur_path = os.path.dirname(__file__)
    file_name = 'resources/access.log'
    len_folder = len(cur_path.split('/')[7])
    len_cur_path = len(cur_path)

    with open(cur_path[0:(len_cur_path - len_folder)] + file_name, 'r') as f:
        current_string = f.readline()
        unique_ip_map: dict = {}
        while current_string != "":
            if current_string.split(' ')[8][0:1] == '5':
                if unique_ip_map.get(current_string.split(' ')[0]) is None:
                    unique_ip_map[current_string.split(' ')[0]] = 0
                else:
                    temp_var = unique_ip_map.get(current_string.split(' ')[0]) + 1
                    unique_ip_map.update({current_string.split(' ')[0]: temp_var})
            current_string = f.readline()

        marklist = sorted(unique_ip_map.items(), key=operator.itemgetter(1), reverse=True)
        sortdict = dict(marklist)
        top_number = 0
        result_list = []
        for key, value in sortdict.items():
            if top_number != 10:
                temp_list = [key, value]
                result_list.append(temp_list)
            else:
                return result_list
            top_number += 1
