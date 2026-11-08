# WHILE


contador = 0;

while contador <= 100:
    contador += 1;

    if contador == 6:
        print("O número 6 foi encontrado, pulando para o próximo número...");
        continue;

    if contador >= 10 and contador <= 27:
        print("Não vou mostar o ", contador);
        continue;

    print(contador);


    if  contador == 40:
        break;