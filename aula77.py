# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
quantidade_acertos = 0;

for pergunta in perguntas:
    print(pergunta['Pergunta'])
    for i, opcao in enumerate(pergunta['Opções']):
        print(f'{i})', opcao)
    resposta_usuario = int(input('Digite sua resposta: '))
    # if resposta_usuario.isdigit():
    #     resposta_usuario = pergunta['Opções'][int(resposta_usuario)]
    if resposta_usuario == pergunta['Resposta']:
        print('Acertou!（￣︶￣）↗')
    else:
        print('Errou! A resposta correta é:', pergunta['Resposta'])
    print()
    
    if acertou:
        quantidade_acertos += 1
        print('Você acertou', quantidade_acertos, 'perguntas.')
    else:
        print('Você errou', quantidade_erros, 'perguntas.')    