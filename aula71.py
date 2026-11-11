# Closure e funções que retornam funções

def criar_saudacao(saudacao):
    def saudar(nome):
        return f"{saudacao}, {nome}!"
    return saudar

saudacao_1 = criar_saudacao("Olá")
saudacao_2 = criar_saudacao("Oi")

print(saudacao_1("Kalli"))  # Olá, Kalli!
print(saudacao_2("Nala"))  # Oi, Nala!