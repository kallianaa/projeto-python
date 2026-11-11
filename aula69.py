# Exercícios com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total


resultado = multiplicar(1, 2, 3, 4, 5)
# print(resultado % 2 == 0)  # True, pois o resultado é 120, que é par

def par_impar(numero):
    if numero % 2 == 0:
        return f"{numero} é par"
    else:
        return f"{numero} é ímpar"

print(par_impar(resultado))  # par