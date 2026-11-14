# Try, except, else e finally

try:
    numero = int(input('Digite um número: '))
    print(f'Você digitou o número {numero}')
except ValueError:
    print('Valor inválido. Digite apenas números.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar o número.')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
except TypeError:
    print('Ocorreu um erro de tipo.')
else:
    print('Código executado com sucesso.')
finally:
    print('Finalizando o programa.')


