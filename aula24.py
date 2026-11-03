# EXERCÍCIO

nome = input('Digite seu nome: ');
idade = int(input('Digite sua idade: '));

# print('Nome:', nome);
# print('Idade:', idade); 

if nome and idade: # Verifica se as variáveis não estão vazias
    print(f'Seu nome é {nome} e sua idade é {idade} anos'); # Interpolação
    print(f'Seu nome invertido é {nome[::-1]}'); # Inverte a string
    
    if ' ' in nome: # Verifica se há espaços em branco no nome
        print('Seu nome contém espaços em branco'); # Espaços em branco no nome
    else:
        print('Seu nome não contém espaços em branco'); # Sem espaços em branco no nome
    
    print(f'Seu nome tem {len(nome)} caracteres'); # Retorna o comprimento da string
    print(f'A primeira letra do seu nome é {nome[0]}'); # Acessa o primeiro caractere da string
    print(f'A última letra do seu nome é {nome[-1]}'); # Acessa o último caractere da string
else:
    print('Você deixou campos vazios, por favor preencha todos os campos.');