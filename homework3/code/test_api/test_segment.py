import pytest

from test_api.segments_base import SegmentsBase


class TestCreateAndDeleteSegment(SegmentsBase):

    @pytest.mark.CreateSegment
    def test_create(self):
        self.check_create_segment()

    @pytest.mark.DeleteSegment
    def test_delete(self):
        self.check_delete_segment()
