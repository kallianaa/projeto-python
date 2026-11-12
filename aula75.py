# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro


pessoa = {
    'nome': 'Kalliana Regina',
    'sobrenome': 'Glaeser',
}

# print(pessoa.__len__());

pessoa.setdefault('idade', 31);
print(pessoa['idade']);

print(list(pessoa.keys()));
print(list(pessoa.values()));
print(list(pessoa.items()));

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(chave, valor)


#
print()
#

print(pessoa.get('nome'));

ultima_chave = pessoa.popitem();
print(ultima_chave);
print(pessoa);

#
print()
#

# pessoa.update({
#     'nome': 'Kalliana', 
#     'idade': 32});

pessoa.update(nome='Nala', idade=6);
print(pessoa);

#
print()
#

tupla = ('nome', 'idade');
print(pessoa.get(tupla[0]));