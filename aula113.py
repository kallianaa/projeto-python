# reduce - faz a redução de um iterável em um único valor 

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def somar_precos(acumulador, produto):
    print(f'acumulador: {acumulador} + produto: {produto["preco"]}')
    return acumulador + produto['preco']

total = reduce(somar_precos, produtos, 0)
print(f'Total: {total:.2f}')