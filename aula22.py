# FORMATAÇÃO DE STRINGS

variavel = "ABC";
print(f'Valor: {variavel}'); # Interpolação
print(f'Valor: {variavel: >10}'); # Alinhamento à direita
print(f'Valor: {variavel: <10}'); # Alinhamento à esquerda
print(f'Valor: {variavel: ^10}'); # Alinhamento ao centro
print(f'Valor: {variavel: >10.3}'); # Alinhamento à direita com limite de caracteres

print(f'{1000.4873648123746:0=+10,.1f}'); # Formatação de números
print(f'O hexadecimal de {1500} é {1500:08x}'); # Formatação de números
print(f'O hexadecimal de {1500} é {1500:08X}'); # Formatação de números