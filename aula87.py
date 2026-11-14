# isinstace() - para saber se objeto é de determinado tipo

lista = ['a', 1, 1.1, True, [0, 1, 2], {'nome': 'Kalliana'}, (1, 2), {0, 1}]

for item in lista:
    if isinstance(item, set):
        print("SET")
        item.add(5)
        print(item, isinstance(item, set))

    elif isinstance(item, str):
        print("STRING")
        print(item.upper(), isinstance(item, str))

    elif isinstance(item, (int, float)):
        print("NUMERO")
        print(item * 2, isinstance(item, (int, float)))
    else:
        print("OUTRO")
        print(item)