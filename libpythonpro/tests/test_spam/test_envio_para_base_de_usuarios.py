from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadorDeSpam


def test_de_spam(sessao):
    enviador_de_spam = EnviadorDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_emails(
        "felipe.antonio.online@proton.me",
        "Curso Python Pro",
        "Veja o que estamos aprendendo.",
    )
