""" EXERCÍCIO

Exiba os indices da lista

0 Nala
1 Pablo
2 Katy

"""

lista = ["Nala", "Pablo", "Katy"];

i = 0;
for nome in lista:
    print(f"{i} {nome}"); # 0 Nala, 1 Pablo, 2 Katy
    i += 1;

#outra solução
indices = range(len(lista)); # range(0, 3)
for indice in indices:
    print(f"{indice} {lista[indice]}"); # 0 Nala, 1 Pablo, 2 Katy