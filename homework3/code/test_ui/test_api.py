import pytest
from base import ApiBase


@pytest.mark("Create")
class TestCreate(ApiBase):

    def test_create_segment(self):
        name_segment = 'testseg'
        res = self.api_client.post_segment_create(name_segment)
        assert name_segment == res['name']
        self.api_client.post_delete_segment(res['id'])


@pytest.mark("Delete")
class TestDelete(TestCreate):

    def test_delete_segment(self):
        super(TestCreate, self).test_create_segment()
