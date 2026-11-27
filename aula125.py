# Escopo da classe e de métodos da classe

class Animal:
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade

    def fazer_som(self):
        print(f'O {self.especie} está fazendo um som.')

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}, sou um {self.especie} e tenho {self.idade} anos.')

# Criando uma instância da classe Animal
animal1 = Animal('Nala', 'Cachorro', 6)
animal1.fazer_som()  # Chama o método fazer_som da instância animal1
animal1.apresentar()  # Chama o método apresentar da instância animal1

