import pytest
import requests


class TestFuzzySearch:
    @pytest.fixture(autouse=True)
    def request_api(self):
        self.url = 'https://regions-test.2gis.com/1.0/regions'

    def test_fuzzy_search_parameters_ignore(self):
        params = {'q': 'Владикавказ', 'code': 'kz'}
        response = requests.get(self.url, params=params, verify=False)
        rdict = response.json()
        for keys in rdict['items']:
            assert keys['country']['code'] == 'ru'

    @pytest.mark.parametrize("params, expected",
                             [({'q': 'мо'}, 'error'),
                              ({'q': 'мос'}, 'items'),
                              ({'q': 'МоскВА'}, 'items')]
                             )
    def test_fuzzy_search_boundaries(self, params, expected):
        response = requests.get(self.url, params=params, verify=False)
        rdict = response.json()
        assert rdict[expected]

    @pytest.mark.parametrize("params",
                             [({'q': '   '}),
                              ({'q': '!!!'}),
                              ({'q': 'Днеп@р'}),
                              ({'q': 'wow'}),
                              ({'q': '123'})]
                             )
    def test_fuzzy_search_equivalence(self, params, expected):
        response = requests.get(self.url, params=params, verify=False)
        rdict = response.json()
        assert len(rdict['items']) == 0
