from Lista import Lista

l = Lista(8) #CRIA A LISTA

print('*'*15)
print('Inserções')
print('*'*15)

l.inserir_na_frente(5) #METODO INICIALIZADOR
print('Garantir inicialização do cursor:')
print(l.acessar_atual().get_valor()) #GARANTIR INICIALIZACAO DO CURSOR
l.inserir_apos_atual(4) #INSERCAO01
l.inserir_apos_atual(3) #INSERCAO02

print('*'*15)
print('Operações de Consulta')
print('*'*15)

print(l.lista_vazia())
print(l.lista_cheia())
print(l.consulta_por_posicao(1))
print(l.acessar_atual().get_valor())

print('*'*15)
print('Inserções')
print('*'*15)

l.inserir_antes_atual(2) #INSERCAO03
print('Garantir atualização do cursor:')
print(l.acessar_atual().get_valor()) #GARANTIR ATUALIZACAO DO CURSOR

print('*'*15)
print('Exclusão')
print('*'*15)

l.excluir_atual() #EXCLUSAO01
print('Garantir atualização do cursor:')
print(l.acessar_atual().get_valor()) #CURSOR DEVE RETORNAR A POSICAO 0
l.excluir_primeiro()
print('Garantir atualização do cursor:')
print(l.acessar_atual().get_valor()) #CURSOR DEVE RETORNAR A POSICAO 0

print('*'*15)
print('Inserção')
print('*'*15)

l.inserir_no_fim(10) #INSERCAO04
print('Garantir atualização do cursor:') #CURSOR DEVE ESTAR NO 10
print(l.acessar_atual().get_valor())
l.inserir_na_posicao(0, 12)  #INSERCAO05
print('Garantir atualização do cursor:')
print(l.acessar_atual().get_valor()) #CURSOR DEVE RETORNAR 
print('Garantir atualização do elemento:')
print(l.consulta_por_posicao(0))
print('Inserir em posição diferente de 0:')
l.inserir_na_posicao(2, 13)
print('Garantir atualização do cursor:')
print(l.acessar_atual().get_valor())
print('Garantir atualização do elemento:')
print(l.consulta_por_posicao(2))

print('*'*15)
print('Exclusão')
print('*'*15)

l.excluir_ultimo()
print('Garantir atualização do cursor:')
print(l.acessar_atual().get_valor()) #CURSOR DEVE ATUALIZAR A NOVA ULTIMA POSICAO

'''
---> CODIGO BUGADO <---
l.excluir_valor(13)
print('Garantir atualização do cursor:')
print(l.acessar_atual().get_valor())

'''
l.excluir_da_posicao(2)
print('Garantir atualização do cursor:')
print(l.acessar_atual().get_valor())

print('*'*15)
print('Busca')
print('*'*15)

print(l.buscar(12))

'''
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
'''