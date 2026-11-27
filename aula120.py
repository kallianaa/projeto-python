# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

import json
import os   

CAMINHO_ARQUIVO = os.path.join(os.path.dirname(__file__), 'aula120_tarefas.json')

def ler(tarefas, caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        salvar(tarefas, caminho_arquivo)
        return tarefas


def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    print(f'{tarefa=} removida da lista de tarefas.')
    tarefas_refazer.append(tarefa)
    print()


def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou uma tarefa.')
        return
    print(f'{tarefa=} adicionada na lista de tarefas.')
    tarefas.append(tarefa)
    print()


tarefas = []
tarefas_refazer = []

CAMINHO_ARQUIVO = 'aula120_tarefas.json'
tarefas = ler([], CAMINHO_ARQUIVO)
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer ou sair')
    tarefa = input('Digite uma tarefa ou comando: ')
    comando = tarefa.strip().lower()

    if comando == 'listar':
        listar(tarefas)
    elif comando == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        salvar(tarefas, CAMINHO_ARQUIVO)
    elif comando == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        salvar(tarefas, CAMINHO_ARQUIVO)
    elif comando == 'sair':
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        salvar(tarefas, CAMINHO_ARQUIVO)