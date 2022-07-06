import requests


def busca_avatar(usuario):
    """
    Encontra e retorna a url do avatar do usuário do github."""

    url = f"https://api.github.com/users/{usuario}"
    resp = requests.get(url)
    return resp.json()["avatar_url"]
