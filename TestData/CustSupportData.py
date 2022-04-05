import pytest


class CustSupportData:
    @pytest.fixture(
        params=[{"ReachingOutMessage": "Someone will get back to you soon",
                 }])
    def customerSupportData(self, request):
        return request.param