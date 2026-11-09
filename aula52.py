"""
EXERCÍCIO 
    - Faça uma lista de compras com listas;
    - O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista;
    - Não permita que o programa quebre com erros de índices inexistentes na lista.
"""
import os

lista_compras = [];

while True:
    print("Escolha uma opção:");
    print("1 - Adicionar item");
    print("2 - Remover item");
    print("3 - Listar itens");
    print("4 - Sair");

    opcao = input("Digite a opção desejada: ");

    if opcao == "1":
        os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela
        item = input("Digite o item que deseja adicionar: ");
        lista_compras.append(item);
        print(f"{item} adicionado à lista de compras.");
    
    elif opcao == "2":
        os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela
        item = input("Digite o item que deseja remover: ");
        if item in lista_compras:
            lista_compras.remove(item);
            print(f"{item} removido da lista de compras.");
        else:
            print(f"{item} não encontrado na lista de compras.")
    
    elif opcao == "3":
        os.system("cls" if os.name == "nt" else "clear")  # Limpa a tela
        if len(lista_compras) == 0:
            print("A lista de compras está vazia.")
        else:
            print("Itens na lista de compras:")
            for i, item in enumerate(lista_compras):
                print(f"{i + 0}. {item}")
    
    elif opcao == "4":
        print("Saindo do programa.")
        break
    
    else:
        print("Opção inválida. Tente novamente.")