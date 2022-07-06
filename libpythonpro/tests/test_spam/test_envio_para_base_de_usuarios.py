import pytest
from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam
from libpythonpro.spam.modelos import Usuario


class EnviadorMock(Enviador):
    def __init__(self):
        super().__init__()
        self.qtde_emails_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtde_emails_enviados += 1


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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        "felipe.antonio.online@proton.me",
        "Curso Python Pro",
        "Veja o que estamos aprendendo.",
    )
    assert len(usuarios) == enviador.qtde_emails_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome="Felipe", email="felipe.antonio.online@proton.me")
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadorDeSpam(sessao, enviador)
    enviador_de_spam.enviar_emails(
        "foo@proton.me",
        "Curso Python Pro",
        "Veja o que estamos aprendendo.",
    )
    assert enviador.parametros_de_envio == (
        "foo@proton.me",
        "felipe.antonio.online@proton.me",
        "Curso Python Pro",
        "Veja o que estamos aprendendo.",
    )
