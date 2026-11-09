# Itevável -> str, range, list, tuple, set, dict
# Iterador -> quem sabe entra um valor por vez
# next -> me entrega o próximo valor
# iter -> me entrega seu iterador


# numeros = range(0, 100, 8);

# for numero in numeros:
#     print(numero);

# texto = iter("Kalliana") # __iter__() -> iterador
# print(texto);
# print(next(texto)); # __next__() -> próximo valor
# print(texto.__next__()); # __next__() -> próximo valor

# for letra in texto:
texto = "Kalliana"; #itervável
iterador = iter(texto); #iterator

while True:
    try:
        print(next(iterador));
    except StopIteration:
        break;    

# for por debaixo dos panos é um while True com try e except StopIteration
for letra in texto:
    print(letra);