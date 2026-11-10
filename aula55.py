# LISTAS DE LISTAS E SEUS ÍNDICES

salas = [
    # 0       1
    ["Nala", "Pablo"], # 0
    # 0
    ["Kalliana"], # 1
    # 0         1         2      
    ["Thainá", "Python", "Katy"] # 2
]

# print(salas[0][1]);
# print(salas[1][0]);
# print(salas[2][2]);
# print(salas[2][1]);


for sala in salas:
    print("Sala: ", sala);
    for aluno in sala:
        print(aluno);