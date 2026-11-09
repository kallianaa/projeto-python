# WHILE COM ITERAÇÃO

frase = "O Python é uma linguagem de programação multiparadigma. " \
        "Python foi criado por Guido van Rossum e lançado em 1991.";

print(frase.count("Python"));

i = 0;
qtd_apareceu_mais_vezes = 0;
letra_apareceu_mais_vezes = "";
while i < len(frase):
    letra_atual = frase[i];

    if letra_atual == " ":
        i += 1;
        continue;
    
    quanta_vezes_letra_aparece_atual = frase.count(letra_atual);
    
    if qtd_apareceu_mais_vezes < quanta_vezes_letra_aparece_atual:
        qtd_apareceu_mais_vezes = quanta_vezes_letra_aparece_atual;
        letra_apareceu_mais_vezes = letra_atual;

    i += 1;
print(f"A letra que apareceu mais vezes foi: {letra_apareceu_mais_vezes}, aparecendo {qtd_apareceu_mais_vezes} vezes.");
