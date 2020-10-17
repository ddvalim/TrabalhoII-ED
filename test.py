from Lista import Lista

l = Lista(5)

l.inserir_na_frente(5)
l.inserir_apos_atual(4)
l.inserir_apos_atual(3)
assert l.acessar_atual().get_valor() == 3 
l.inserir_antes_atual(2)
assert l.acessar_atual().get_valor() == 2
el = l.acessar_atual()
l.ir_para_final()
assert el != l.acessar_atual()
assert l.buscar(2)
assert l.buscar(5)
assert not l.buscar(77)
l.excluir_primeiro()
l.ir_para_inicio()
assert l.acessar_atual().get_valor() == 4
l.excluir_ultimo()
l.ir_para_final()
assert l.acessar_atual().get_valor() == 2