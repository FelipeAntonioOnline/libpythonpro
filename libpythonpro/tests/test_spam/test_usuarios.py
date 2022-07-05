from libpythonpro.spam.modelos import Usuario


def test_salvar_usuario(sessao):
    usuario = Usuario(nome="Felipe", email="felipe.antonio.online@proton.me")
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)


def test_listar_usuario(sessao):
    usuarios = [
        Usuario(nome="Felipe", email="felipe.antonio.online@proton.me"),
        Usuario(nome="Antonio", email="foo@bar"),
    ]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuarios == sessao.listar()
