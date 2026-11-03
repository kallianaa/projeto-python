# FATIAMENTO DE STRINGS
# 0123456789
# Olá, mundo
#-9876543210

variavel = "Olá, mundo!";
print(variavel[0]); # Acessa o primeiro caractere da string
print(variavel[1:5]); # Acessa os caracteres de índice 1 a 4
print(variavel[7:]); # Acessa os caracteres a partir do índice 7
print(variavel[:5]); # Acessa os caracteres até o índice 4
print(variavel[-1]); # Acessa o último caractere da string
print(variavel[-5:-1]); # Acessa os caracteres de índice -5 a -2
print(variavel[0:9:2]); # Acessa os caracteres de índice 0 a 9, pulando de 2 em 2

# FUNÇÃO LEN

print(len(variavel)); # Retorna o comprimento da string