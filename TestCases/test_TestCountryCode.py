import pytest
import requests


class TestFuzzySearch:
    @pytest.fixture(autouse=True)
    def request_api(self):
        self.url = 'https://regions-test.2gis.com/1.0/regions'

    @pytest.mark.parametrize("params",
                             [({'country_code': 'ru'}),
                              ({'country_code': 'kg'}),
                              ({'country_code': 'kz'}),
                              ({'country_code': 'cz'})]
                             )
    def test_country_code_positive(self, params):
        response = requests.get(self.url, params=params, verify=False)
        rdict = response.json()
        for keys in rdict['items']:
            assert keys['country']['code'] == params['country_code']

    def test_country_code_negative(self):
        response = requests.get(
            self.url, params={'country_code': 'ua'}, verify=False)
        rdict = response.json()
        assert rdict['error']