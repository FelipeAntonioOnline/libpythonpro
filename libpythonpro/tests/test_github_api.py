from unittest.mock import Mock

import pytest
from libpythonpro import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    url = "https://avatars.githubusercontent.com/u/mock"
    resp_mock.json.return_value = {
        "login": "FelipeAntonioOnline",
        "id": 100208168,
        "avatar_url": url,
    }
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield url
    github_api.requests.get = get_original


def test_busca_avatar(avatar_url):
    url = github_api.busca_avatar("fao_mock")
    assert avatar_url == url


def test_busca_avatar_integracao():
    url = github_api.busca_avatar("felipeantonioonline")
    assert "https://avatars.githubusercontent.com/u/100208168?v=4" == url
