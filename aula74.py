# Manipulando chaves e valores em dicionários

pessoa = {}

##
##

chave = 'nome'

pessoa[chave] = 'Kalliana Regina'
pessoa['sobrenome'] = 'Glaeser'


print(pessoa[chave])

pessoa[chave] = 'Thainá'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')