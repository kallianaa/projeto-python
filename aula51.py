# enumerate - enumeração iteráveis (índices)

lista = ["Nala", "Pablo", "Katy"];
lista.append("Kalliana");

lista_enumerada = list(enumerate(lista)); # cria uma lista enumerada
print(lista_enumerada); # [(0, 'Nala'), (1, 'Pablo'), (2, 'Katy'), (3, 'Kalliana')]

for item in lista_enumerada:
    indice, nome = item; # desempacotamento da tupla
    print(indice, nome); 

