from unittest.mock import Mock
from libpythonpro import github_api


def test_busca_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        "login": "FelipeAntonioOnline",
        "id": 100208168,
        "avatar_url": "https://avatars.githubusercontent.com/u/100208168?v=4",
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.busca_avatar("felipeantonioonline")
    assert "https://avatars.githubusercontent.com/u/100208168?v=4" == url
