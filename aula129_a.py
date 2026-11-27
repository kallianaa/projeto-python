# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON e depois crie novamente as instâncias da classe com os dados salvos 
# Faça em arquivos separados.

import json

CAMINHO_ARQUIVO = "aula129.json"

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade  # Atributo de instância

    def apresentar(self):
        print(f'Olá, meu nome é {self.nome}, tenho {self.idade} anos.')

pessoa1 = Pessoa('Kalli', 31)
pessoa2 = Pessoa('Nala', 6)
pessoa3 = Pessoa('Thainá', 32)
banco_dados = [pessoa1.__dict__, pessoa2.__dict__, pessoa3.__dict__]



with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(banco_dados, arquivo, ensure_ascii=False, indent=2)  # Salva os dados em JSON no arquivo aula129.json


def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
        print("Fazendo dump dos dados em JSON...")
        json.dump(banco_dados, arquivo, ensure_ascii=False, indent=2)  # Salva os dados em JSON no arquivo aula129.json

if __name__ == "__main__":
    print("ELE é o tal do __main__")
    fazer_dump()  # Chama a função fazer_dump para salvar os dados em JSON