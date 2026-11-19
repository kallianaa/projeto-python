# Decoradores com parâmetros
def fabrica_decoradores(a=None, b=None, c=None):
    def fabrica_de_funcoes(func):
        print("Decoradora foi executada.")

        def aninhada(*args, **kwargs):
            print("Aninhada foi executada.")
            return func(*args, **kwargs)
        return aninhada
    return fabrica_de_funcoes
    

@fabrica_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

decoradora = fabrica_decoradores()
multiplicadora = decoradora(lambda x, y: x * y)

dez_mais_cinco = soma(10, 5)
dez_vezes_cinco = multiplicadora(10, 5)

print(dez_mais_cinco)  # Saída: 15
print(dez_vezes_cinco)  # Saída: 50