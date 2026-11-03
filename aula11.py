# formantando Strings

nome = "Kalliana Glaeser";
altura = 1.77;
peso = 76;
imc = peso / (altura ** 2);


# f-strings
linha_1 = "{} tem {} de altura e pesa {} quilos e seu IMC é de {}".format(nome, altura, peso, imc);

linha_2 = f"{nome} tem {altura:.2f} de altura e pesa {peso} quilos e seu IMC é de {imc:.2f}";

print(linha_1);
print(linha_2);