# EXERCÍCIO

"""
Crie uma função que duplicam, triplicam e quadruplicam o valor recebido como parâmetro.
"""
valor = input("Digite um valor: ")
valor = int(valor)


# def duplicar(valor):
#     return valor * 2

# def triplicar(valor):
#     return valor * 3

# def quadruplicar(valor):
#     return valor * 4

# print(duplicar(valor))  # 10
# print(triplicar(valor))  # 15   
# print(quadruplicar(valor))  # 20


def criar_multiplicador(multiplicador):
    def multiplicar(valor):
        return valor * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(valor))  # 10
print(triplicar(valor))  # 15
print(quadruplicar(valor))  # 20
