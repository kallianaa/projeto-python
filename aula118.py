# Problema dos parâmetros mutáveis em funções

def adiciona_cliente(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

lista1 = []

clientes1 = adiciona_cliente('Kalliana')
clientes1.append('Thainá')
print(clientes1)  # ['Kalliana']

clientes2 = adiciona_cliente('Pablo')
print(clientes2)  # ['Kalliana', 'Pablo']

adiciona_cliente('Nala', clientes2)
print(clientes2)  # ['Kalliana', 'Pablo', 'Nala']

