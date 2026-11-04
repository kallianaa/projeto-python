# WHILE

condicao = True;

while condicao:
    nome = input("Qual o seu nome? ");
    print(f"Olá {nome}!");
    if nome == "sair":
        break;