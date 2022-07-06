from unittest.mock import Mock
import pytest
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


@pytest.mark.parametrize(
    "usuarios",
    [
        [
            Usuario(nome="Felipe", email="felipe.antonio.online@proton.me"),
            Usuario(nome="Antonio", email="foo@bar"),
        ],
        [
            Usuario(nome="Felipe", email="felipe.antonio.online@proton.me"),
        ],
    ],
)
def test_qtde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        "felipe.antonio.online@proton.me",
        "Curso Python Pro",
        "Veja o que estamos aprendendo.",
    )
    assert len(usuarios) == enviador.enviar.call_count


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome="Felipe", email="felipe.antonio.online@proton.me")
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        "foo@proton.me",
        "Curso Python Pro",
        "Veja o que estamos aprendendo.",
    )
    enviador.enviar.assert_called_once_with == (
        "foo@proton.me",
        "felipe.antonio.online@proton.me",
        "Curso Python Pro",
        "Veja o que estamos aprendendo.",
    )
