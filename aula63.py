"""
Argumentos nomeados (keyword arguments) e não nomeados (positional arguments) em funções Python.
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y):
    print(f"{x=} {y=}", "|", "x + y =", x+y);
soma(1, 2);