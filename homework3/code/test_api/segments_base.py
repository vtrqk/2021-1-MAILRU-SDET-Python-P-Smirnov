from test_api.base import ApiBase


class SegmentsBase(ApiBase):

    def check_create_segment(self):
        name_segment = self.builder.create_segment()
        result = self.api_client.post_segment_create(name_segment=name_segment.name)
        assert result['id']
        self.api_client.post_delete_segment(result['id'])

    def check_delete_segment(self):
        name_segment = self.builder.create_segment()
        result_create = self.api_client.post_segment_create(name_segment=name_segment.name)
        result_delete = self.api_client.post_delete_segment(result_create['id'])
        assert result_delete['successes'][0]['source_id'] == result_create['id']
