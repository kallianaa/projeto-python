# operadores Logicos (and, or, not)
# AND - todas as condições precisam ser verdadeiras para retornar True
# OR - pelo menos uma das condições precisa ser verdadeira para retornar True
# NOT - inverte o valor booleano da expressão

entrada = input("[E]ntrar [S]air: ");
senha_digitada = input("Senha: ");

senha_permitida = "123456";

# IF condicao só sera executada quando for verdadeira
if entrada == "E" and senha_digitada == senha_permitida:
     print("Entrar");
elif entrada == "S":
    print("Sair");
else:
    print("Opção inválida.");



print(True and True and True); # True
print(True and False); # False
print(False and True); # False
print(False and False); # False

if 1 and 1:
    print(True and 1 and False)