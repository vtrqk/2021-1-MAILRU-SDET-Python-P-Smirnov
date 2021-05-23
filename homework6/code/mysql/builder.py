from utils.favorite_requests import get_top_favorite_requests
from utils.count_post_and_get import count_post_and_get
from utils.count_all_requests import count_all_requests
from utils.largest_requests import get_largest_requests
from utils.top_5_users import get_top_users
from mysql.models import PostAndGet, AllRequests, FavoriteRequests, LargestReq, TopUsers


class MySQLBuilder:

    def __init__(self, client):
        self.client = client

    def create_favorite_req(self):
        list_requests = get_top_favorite_requests()
        for i in range(10):
            name_url, count = list_requests[i]

            favorite_model = FavoriteRequests(
                name_url=name_url,
                count=count
            )
            self.client.session.add(favorite_model)
            self.client.session.commit()

    def create_post_and_get(self):
        list_requests = count_post_and_get()
        post_and_get_model = PostAndGet(
            get_count=list_requests[0],
            post_count=list_requests[1]
        )
        self.client.session.add(post_and_get_model)
        self.client.session.commit()

    def create_top_users(self):
        list_requests = get_top_users()

        for i in range(5):
            ip_user, count = list_requests[i]

            top_users_model = TopUsers(
                ip_user=ip_user,
                count=count
            )
            self.client.session.add(top_users_model)
            self.client.session.commit()

    def create_all_requests(self):
        result = count_all_requests()
        all_requests_model = AllRequests(
            count_all=result
        )
        self.client.session.add(all_requests_model)
        self.client.session.commit()

    def create_largest_requests(self):
        list_requests = get_largest_requests()
        for i in range(5):
            ip_req, name_url, code_err, size = list_requests[i]

            largest_model = LargestReq(
                ip_req=ip_req,
                name_url=name_url,
                code_err=code_err,
                size=size
            )
            self.client.session.add(largest_model)
            self.client.session.commit()
