"""
split e join com list e str
split - divide uma string em uma lista de strings
join - junta uma lista de strings em uma única string
"""

frase = "Python é uma linguagem de programação, e é muito utilizada para desenvolvimento web, ciência de dados, automação e muito mais.";
lista_frases_cruas = frase.split(); # divide a string em uma lista de palavras
print(lista_frases_cruas); # ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']

lista_frases = frase.split(","); # divide a string em uma lista de frases
print(lista_frases); # ['Python é uma linguagem de programação', ' e é muito utilizada para desenvolvimento web', ' ciência de dados', ' automação e muito mais.']


lista_frases = [];
for i, frase in enumerate(lista_frases_cruas):
    print(f"Frase {i + 1}: {frase.strip()}"); # strip remove espaços em branco no início e no final da string
    lista_frases.append(frase.strip());

frases_unidas = " ".join(lista_frases_cruas); # junta a lista de palavras em uma única string
print(frases_unidas); # Python é uma linguagem de programação, e é muito utilizada para desenvolvimento web, ciência de dados, automação e muito mais.