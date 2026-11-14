# Introdução a Generators functions em Python
# generator = (n for n in range(10))

# def generator(n=0):
#     yield 1 # pausado, retorna o valor e mantém o estado da função
#     print('Continuando...')
#     yield 2 # pausado, retorna o valor e mantém o estado da função
#     print("Mais uma coisa...")
#     yield 3 # pausado, retorna o valor e mantém o estado da função
#     print('Vou terminar.')
#     return 'Acabou' # finaliza a função, não retorna o valor


def generator(n=0, max=10):
    while True:
        yield n
        n += 1

        if n >= max:
            return


gen = generator(n=0)
for n in gen:
    print(n)