# Entendendo self em classes

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.')

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa('Kalli', 31)
pessoa1.apresentar()  # Chama o método apresentar da instância pessoa1