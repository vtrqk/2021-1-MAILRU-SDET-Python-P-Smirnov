import operator
import os


def get_top_favorite_requests():

    file_access_path = 'resources/access.log'

    with open(os.path.join(os.path.dirname(os.getcwd()), file_access_path), 'r') as f:
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
        result_list = []
        for key, value in sortdict.items():
            if top_number != 10:
                if top_number != 10:
                    temp_list = [key, value]
                    result_list.append(temp_list)
            else:
                return result_list
            top_number += 1
