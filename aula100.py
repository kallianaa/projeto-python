# Exercícios

import copy
from dados import produtos

# # copy, sorted, produtos.sort

# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]


# produtos = [
#     {'nome': 'Produto 5', 'preco': 10.00},
#     {'nome': 'Produto 1', 'preco': 22.32},
#     {'nome': 'Produto 3', 'preco': 10.11},
#     {'nome': 'Produto 2', 'preco': 105.87},
#     {'nome': 'Produto 4', 'preco': 69.90},
# ]

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)


# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
)

print("Produtos originais", *produtos, sep='\n')
print()
print("Novos produtos", *novos_produtos, sep='\n')
print()
print("Produtos ordenados por nome", *produtos_ordenados_por_nome, sep='\n')
print()
print("Produtos ordenados por preco", *produtos_ordenados_por_preco, sep='\n')
