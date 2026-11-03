# INTRODUÇÃO AO TRY/EXCEPT
# try -> tentar executar o código
# except -> ocorreu algum erro ao tentar executar o código

numero_str = input('Vou dobrar o número que você digitar: ');


try:
    numero_float = float(numero_str);
    print(f'O dobro de {numero_float} é {numero_float * 2}');
    print(f'Você digitou o número {numero_float}');
except ValueError:
    print('Isso não é um número válido!');