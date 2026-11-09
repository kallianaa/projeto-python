# LISTAS
# Tipo list - Mutável
# Métodos úteis: append, insert, pop, del, clear, extend, +, *, min, max, sum, sorted, sort

string = "ABCDE"; # 5 caracteres (len)

#        0    1      2                  3    4
#       -5   -4     -3                 -2   -1
lista = [123, True, "Kalliana Glaeser", 1.2, []];
print(lista[2]); # Kalliana Glaeser

lista[2] = "Nala"; # Alterando o valor do índice 2
print(lista[2]); # Nala
print(lista); # [123, True, 'Nala', 1.2, []]