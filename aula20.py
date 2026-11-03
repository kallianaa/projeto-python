# operadores IN e NOT IN

nome = "Kalliana";
print(nome[2]);
print(nome[-4]);

print("K" in nome); # True
print("k" in nome); # False
print("K" not in nome); # False
print("k" not in nome); # True

nome_usuario = input("Digite seu nome: ");
encontrar = input("Digite o nome que deseja encontrar: ");

if encontrar in nome:
    print(f'O nome {encontrar} foi encontrado');
else:
    print(f'O nome {encontrar} não foi encontrado');