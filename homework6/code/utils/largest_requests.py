import operator
import os


def get_size(firs_var, second_var):
    if second_var != '-' and second_var[1:2] != 'h' and second_var[1:2] != 'a':
        return firs_var + second_var
    else:
        return firs_var


def get_largest_requests():

    cur_path = os.path.dirname(__file__)
    file_name = 'resources/access.log'
    len_folder = len(cur_path.split('/')[6])
    len_cur_path = len(cur_path)

    with open(cur_path[0:(len_cur_path - len_folder)] + file_name, 'r') as f:
        current_string = f.readline()
        elem_tuple: dict = {}
        unique_ip_map: dict = {}
        while current_string != "":
            if current_string.split(' ')[8][0:1] == '4':
                if unique_ip_map.get(current_string.split(' ')[0]) is None:
                    elem_tuple['url'] = current_string.split(' ')[6]
                    elem_tuple['code'] = current_string.split(' ')[8]
                    elem_tuple['size'] = get_size(current_string.split(' ')[9], current_string.split(' ')[10])
                    unique_ip_map[current_string.split(' ')[0]] = elem_tuple
            current_string = f.readline()
        result_list = []
        top = 0
        for x in unique_ip_map:
            if top < 5:
                temp_list = [x]
                for y in unique_ip_map[x]:
                    temp_list.append(unique_ip_map[x][y])
                    result_list.append(temp_list)
                top += 1

        return result_list
