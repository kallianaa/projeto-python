"""
args - Argumentos não nomeados, são passados para a função na ordem em que foram definidos.
kwargs - Argumentos nomeados, são passados para a função com o nome do parametro.
*- *args (empacotamento e desempacotamento) - Permite passar um número variável de argumentos para a função.
"""

# Lembre-se de desempacotar

x, y, *resto = 1, 2, 3, 4
print(x, y, resto)  # 1 2 [3, 4]

def soma(x, y):
    return x + y;

def soma(*args):
    total = 0;
    for numero in args:
        print(f"{numero=}", "|", "total =", total);
        total += numero;
    return total;

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)  # 6

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)  # 15

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
outra_soma = soma(*numeros)
print(outra_soma)  # 55

print(sum(numeros));

