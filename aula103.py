# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python # usar as funções decoradoras em outras funções.

def criar_funcao(funcao):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        resultado = funcao(*args, **kwargs)
        print(f'Função {funcao.__name__} foi chamada com os argumentos {args}. Resultado: {resultado}')
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    return string[::-1] # Inverte a string

def e_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError('O parâmetro deve ser uma string.')


invertida = inverte_string_checando_parametro('123')
print(invertida)