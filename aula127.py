# Atributos de classes

class Pessoa:
    ano_atual = 2026  # Atributo de classe
    especie = 'Humano'  # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade  # Atributo de instância

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}, tenho {self.idade} anos e sou da espécie {Pessoa.especie}.')

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

# Criando instâncias da classe Pessoa
pessoa1 = Pessoa('Kalli', 31)
print(pessoa1.get_ano_nascimento())  # Chama o método get_ano_nascimento da instância pessoa1