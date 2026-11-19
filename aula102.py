# Variáveis livres + nonlocal (locals, globals, nonlocal)

# def fora():
#     x = 10

#     def dentro():
#         # print(locals())  # Variáveis locais da função 'dentro'
#         print(dentro.__code__.co_freevars)  # Variáveis livres da função 'dentro'
#         return x
#     return dentro

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar):
       nonlocal valor_final
       valor_final += valor_a_concatenar
       return valor_final
    return interna

c = concatenar('Olá, ')
print(c('mundo!'))  # Saída: Olá, mundo!