import os


def count_all_requests():

    file_access_path = 'resources/access.log'

    with open(os.path.join(os.path.dirname(os.getcwd()), file_access_path), 'r') as f:
        count_requests = 0
        while f.readline() != "":
            count_requests += 1
        return count_requests
