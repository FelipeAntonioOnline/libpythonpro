def test_salvar_usuario():
    conexao = Conexao()
    sessao = conexao.gerar_sessao()
    usuario = Usuario(nome="Felipe")
    sessao.salvar(usuario)
    assert isinstance(usuario.id, int)
    sessao.rol_back()
    sessao.fechar()
    conexao.fechar()
