def parametros_decorador(nome):
    def decorador(func):
        print(f"Decorador {nome} foi executado.")
        def sua_nova_funcao(*args, **kwargs):
            print(f"Função {func.__name__} foi chamada com os argumentos {args}.")
            return func(*args, **kwargs)
        return sua_nova_funcao
    return decorador

@parametros_decorador(nome="5")
@parametros_decorador(nome="4")
@parametros_decorador(nome="3")
@parametros_decorador(nome="2")
@parametros_decorador(nome="1")
def soma(x, y):
    return x + y

dez_mais_cinco = soma(10, 5)
print(dez_mais_cinco)  # Saída: 15