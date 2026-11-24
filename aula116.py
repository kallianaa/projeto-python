
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir um arquivo em Python (ele pode ou não existir)

# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)

# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)

# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo

# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load = Lê um arquivo json

#caminho_arquivo = 'C:\\Users\\egla1055\\Criando_Arquivo_Com_Python\\'
caminho_arquivo = 'C:\\Users\\kalli\\OneDrive\\Desktop\\PROJETOS\\PYTHON\\projeto-python\\'

caminho_arquivo += 'aula116.txt'

# arquivo = open(caminho_arquivo, 'w')  # Abre o arquivo para escrita (cria se não existir)

# arquivo.close()  # Fecha o arquivo

with open(caminho_arquivo, 'w') as arquivo:  # Abre o arquivo para escrita (cria se não existir)
    arquivo.write('Olá mundo\n')
    arquivo.write('Hello World\n')
    arquivo.writelines(('Linha 1\n', 'Linha 2\n', 'Linha 3\n'))  # Escreve várias linhas
    arquivo.seek(0, 0)  # Move o cursor para o início do arquivo
    # print(arquivo.read())  # Lê o arquivo e imprime na tela 1
    print("Lendo o arquivo com readlines:")
    arquivo.seek(0, 0)
    print(arquivo.readline())  # Lê o arquivo e imprime na tela 2
print('#' * 10)

with open(caminho_arquivo, 'r') as arquivo:  # Abre o arquivo para leitura
    print(arquivo.read())  # Lê o arquivo e imprime na tela 3