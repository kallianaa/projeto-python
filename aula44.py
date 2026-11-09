"""
Listas em Python

Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento

Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas

Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""

#        0   1   2   3
lista = [10, 20, 30, 40];
print(lista);

lista.append(50); # Adiciona um elemento no final da lista
print(lista); # [10, 20, 30, 40, 50]

nome = lista.pop(); # Remove o último elemento da lista
print(lista); # [10, 20, 30, 40]

del lista[-1]; # apaga o último elemento da lista
print(lista); # [10, 20, 30]

lista.insert(2, 25); # Adiciona um elemento na posição do index escolhido 2
print(lista); # [10, 20, 25, 30]

# lista.clear(); # limpa a lista