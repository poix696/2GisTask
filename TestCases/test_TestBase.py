import pytest
import requests

@pytest.fixture()
def api_address():
    return requests.get('https://regions-test.2gis.com/1.0/regions', verify=False)


class TestBase:
    @pytest.fixture(autouse=True)
    def request_api(self, api_address):
        self.response = api_address

    def test_api_is_available(self):
        assert self.response.ok

    def test_total_count(self):
        rdict = self.response.json()
        assert rdict['total'] == 22

    def test_default_count(self):
        rdict = self.response.json()
        assert len(rdict['items']) == 15
