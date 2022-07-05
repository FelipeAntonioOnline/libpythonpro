class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if "@" not in remetente:
            raise EmailInvalido(f"Formato de email inválido: {remetente}")
        return remetente


class EmailInvalido(Exception):
    pass
