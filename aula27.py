# EXERCÍCIO - AULA 55

"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este número é par ou ímpar. 
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
"""

numero = input("Digite um número inteiro: ");
try:
    numero = int(numero)
    if numero % 2 == 0:
        print("O número é par.");
    else:
        print("O número é ímpar.");
except ValueError:
    print("O valor digitado não é um número inteiro.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito, exiba a saudação apropriada. 
Ex.: Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = int(input("Digite a hora atual (0-23): "));
if 0 <= hora <= 11:
    print("Bom dia");
elif 12 <= hora <= 17:
    print("Boa tarde");
elif 18 <= hora <= 23:
    print("Boa noite");
else:
    print("Hora inválida. Por favor, digite um valor entre 0 e 23.");


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto"; 
se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input("Digite seu primeiro nome: ");
if len(nome) <= 4:
    print("Seu nome é curto");
elif 5 <= len(nome) <= 6:
    print("Seu nome é normal");
else:
    print("Seu nome é muito grande");

