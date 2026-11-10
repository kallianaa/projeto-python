# DESCOMPACOTAMENTO EM CHAMADAS DE MÉTODOS E FUNÇÕES

string = "ABCD";
lista = ["MARIA", "HELENA", 1, 2, 3, "EDUARDA"];
tupla = "Python", "é", "legal";

print(*string);
print(*lista);
print(*tupla);


salas = [
    # 0       1
    ["Nala", "Pablo"], # 0
    # 0
    ["Kalliana"], # 1
    # 0         1         2      
    ["Thainá", "Python", "Katy"] # 2
]

print(*salas, sep='\n');