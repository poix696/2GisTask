import pytest
import requests


class TestFuzzySearch:
    @pytest.fixture(autouse=True)
    def request_api(self):
        self.url = 'https://regions-test.2gis.com/1.0/regions'

    @pytest.mark.parametrize("params",
                             [({'page': 0}),
                              ({'page': 4})]
                             )
    def test_page_size_negative(self, params):
        response = requests.get(self.url, params=params, verify=False)
        rdict = response.json()
        assert len(rdict['items']) == 0

    @pytest.mark.parametrize("params",
                             [({'page': ' '}),
                              ({'page': 'III'}),
                              ({'page': '0.5'}),
                              ({'page': '***'})]
                             )
    def test_page_size_negative2(self, params):
        response = requests.get(self.url, params=params, verify=False)
        rdict = response.json()
        assert rdict['error']
