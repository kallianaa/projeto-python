import json

from aula129_a import CAMINHO_ARQUIVO, Pessoa, fazer_dump

fazer_dump()  # Chama a função fazer_dump do módulo aula129_a para salvar os dados em JSON

with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    pessoas = json.load(arquivo)  # Carrega os dados do arquivo aula129.json
    pessoa1 = Pessoa(**pessoas[0])  # Cria uma instância da classe Pessoa com os dados do primeiro dicionário
    pessoa2 = Pessoa(**pessoas[1])  # Cria uma instância da classe Pessoa com os dados do segundo dicionário
    pessoa3 = Pessoa(**pessoas[2])  # Cria uma instância da classe Pessoa com os dados do terceiro dicionário
    
    print(pessoa1.__dict__)  # Imprime o dicionário de atributos da instância pessoa1
    print(pessoa2.__dict__)  # Imprime o dicionário de atributos da instância pessoa2
    print(pessoa3.__dict__)  # Imprime o dicionário de atributos da instância pessoa3
    pessoa1.apresentar()  # Chama o método apresentar da instância pessoa1
    pessoa2.apresentar()  # Chama o método apresentar da instância pessoa2
    pessoa3.apresentar()  # Chama o método apresentar da instância pessoa3


print(__name__)  # Imprime o nome do módulo atual