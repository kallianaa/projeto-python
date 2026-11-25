import json

# pessoa = {
#     'nome': 'Kalliana',
#     'sobrenome': 'Silva',
#     'endereco': [
#         {'rua': 'Rua 1', 'numero': 123},
#         {'rua': 'Rua 2', 'numero': 456},
#     ],
#     'altura': 1.77,
#     'numeros_preferidos': (2, 3, 5, 7, 11),
#     'dev': True,
#     'nada': None,
# }

# with open('aula117.json', 'w', encoding='utf8') as arquivo:
#     json.dump(pessoa, arquivo, ensure_ascii=False, indent=2)  # Gera um arquivo json

with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)  # Lê um arquivo json
    print(pessoa)

