# operadores Logicos (and, or, not)
# AND - todas as condições precisam ser verdadeiras para retornar True
# OR - pelo menos uma das condições precisa ser verdadeira para retornar True
# NOT - inverte o valor booleano da expressão

entrada = input("[E]ntrar [S]air: ");
senha_digitada = input("Senha: ");

senha_permitida = "123456";

# IF condicao só sera executada quando for verdadeira
if (entrada == "E" or entrada == "e") and senha_digitada == senha_permitida:
     print("Entrar");
elif entrada == "S" or entrada == "s":
    print("Sair");
else:
    print("Opção inválida.");

print(True or False); # True
print(False or True); # True
print(True or True); # True
print(False or False); # False
