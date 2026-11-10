"""
Valores padrão de parametros em funções Python.
Ao definir uma função, os parametros podem ter valores padrão.
Caso o valor do parametro não seja passado, o valor padrão será utilizado.
"""

def soma(x, y=0):
    print(f"{x=} {y=}", "|", "x + y =", x+y);