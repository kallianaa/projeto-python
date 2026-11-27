# Métodos em instâncias de classes

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def acelerar(self):
        print(f'O carro {self.marca} {self.modelo} está acelerando...')

    def frear(self):
        print(f'O carro {self.marca} {self.modelo} está freiando...')

# Criando uma instância da classe Carro
meu_carro = Carro('Toyota', 'Corolla')
print(f'Meu carro é um {meu_carro.marca} {meu_carro.modelo}.')
meu_carro.acelerar()
meu_carro.frear()