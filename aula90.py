import sys

# Generator expression, Iterables e Iterators em Python

iterable = ['Kalliana', 'Python', 'JavaScript', 'C#', 'Java']
iterator = iter(iterable)
lista = [item for item in iterable] # list comprehension
generator = [(n for n in range(10))] # generator expression

print(f'Tamanho da lista: {sys.getsizeof(lista)} bytes')
print(f'Tamanho do generator: {sys.getsizeof(generator)} bytes')

# um valor por vez, até que o iterador seja esgotado
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

for n in generator:
    print(n)
