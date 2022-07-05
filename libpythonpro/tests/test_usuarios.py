def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome="Felipe")
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.rol_back()
    sessao.fechar()
    conexao.fechar()


def test_listar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuarios = [Usuario(nome="Felipe"), Usuario(nome="Antonio")]
    for usuario in usuarios:
        sessao.salvar(usuario)
    assert usuario == sessao.listar()
    sessao.rol_back()
    sessao.fechar()
    conexao.fechar()
