# EXERCICIO WHILE
#       0123456789101112131415
nome = "Kalliana Glaeser";

indice = 0;

# while indice < tamanho_nome:
#     print(f"Índice: {indice} - Caractere: {nome[indice]}");
#     indice += 1;

# print("Fim do programa.");

# while indice < len(nome):
#     print(f"Índice: {indice} - Caractere: {nome[indice]}");
#     indice += 1;
# print("Fim do programa.");

novo_nome = "";
while indice < len(nome):
    letra = nome[indice];
    novo_nome += f"*{letra}";
    indice += 1;

novo_nome += "*";
print(novo_nome);
