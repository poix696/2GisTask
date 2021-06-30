import pytest
import requests


class TestFuzzySearch:
    @pytest.fixture(autouse=True)
    def request_api(self):
        self.url = 'https://regions-test.2gis.com/1.0/regions'

    @pytest.mark.parametrize("params",
                             [({'page_size': 5}),
                              ({'page_size': 10}),
                              ({'page_size': 15})]
                             )
    def test_page_size_positive(self, params):
        response = requests.get(self.url, params=params, verify=False)
        rdict = response.json()
        assert len(rdict['items']) == params['page_size']

    @pytest.mark.parametrize("params",
                             [({'page_size': ' '}),
                              ({'page_size': 'пять'}),
                              ({'page_size': '%'}),
                              ({'page_size': '16'}),
                              ({'page_size': '0'})]
                             )
    def test_page_size_negative(self, params):
        response = requests.get(self.url, params=params, verify=False)
        rdict = response.json()
        assert rdict['error']
