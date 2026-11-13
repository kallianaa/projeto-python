# EMPACOTAMENTO E DESEMPACOTAMENTO DE DICIONÁRIOS

a, b = 1, 2;
a, b = b, a;

# print(a, b);

pessoa = {
    'nome': 'Kalliana',
    'sobrenome': 'Glaeser',
}

print(pessoa)

print(pessoa.values())
print(pessoa.items())

# for chave, valor in pessoa.items():
#     print(chave, valor)


dados_pessoa = {
    'idade': 31,
    "altura": 1.77,
}

pessoas_completas = {**pessoa, **dados_pessoa}
print(pessoas_completas)

# args e kwargs
# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
        print(chave, valor)

# mostro_argumentos_nomeados(1, 2, 3, nome='Kalliana', sobrenome='Glaeser')
# mostro_argumentos_nomeados(**pessoas_completas)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}

mostro_argumentos_nomeados(**configuracoes)