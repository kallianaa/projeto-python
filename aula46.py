"""
Cuidados com dados mutáveis - Copy e Deep Copy
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor (mutáveis)
"""

lista_a = ["Kalliana", "Nala"];
lista_b = lista_a; # Aponta para o mesmo valor (mutável)
lista_b = lista_a.copy(); # Copia o valor (imutável)
print(lista_b); # ['Kalliana', 'Nala']

lista_a[0] = "Glaeser"; # Alterando o valor do índice 0 da lista_a
print(lista_b); # ['Kalliana', 'Nala']

