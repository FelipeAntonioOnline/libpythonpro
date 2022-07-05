import pytest
from spam.enviador_de_email import Enviador, EmailInvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize(
    "remetente", ["felipe.antonio.online@proton.me", "foo@bar.com"]
)
def test_remetente(remetente):
    enviador = Enviador()
    resultado = enviador.enviar(
        remetente,
        "felipe23antonio@gmail.com",
        "Curso Python Tools",
        "Teste para verificar a funcionalidade de Enviado.enviar()",
    )
    assert remetente in resultado


@pytest.mark.parametrize("remetente", ["felipe.antonio.online", ""])
def test_remetente_invalido(remetente):
    enviador = Enviador()
    with pytest.raises(EmailInvalido):
        enviador.enviar(
            remetente,
            "felipe23antonio@gmail.com",
            "Curso Python Tools",
            "Teste para verificar a funcionalidade de Enviado.enviar()",
        )
