"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF, MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
    77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
    363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
    3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

import re;
import sys;

# cpf = '36440847007'  # Esse CPF gera o primeiro dígito como 10 (0)
# cpf = "746.824.890-70" \ 
#     .replace(".", "") \
#     .replace(".", "") \
#     .replace("-", "");

entrada_cpf = input("Digite o CPF: ");
cpf = re.sub(r'[^0-9]', '', entrada_cpf);

entrada_e_sequencial = entrada_cpf == entrada_cpf[0] * len(entrada_cpf);

if entrada_e_sequencial == entrada_cpf:
    print("Você digitou um CPF sequencial inválido!");
    sys.exit();

nove_digitos = cpf[:9];
contador_regressivo_1 = 10;

resultado_digito_1 = 0;
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1;
    contador_regressivo_1 -= 1;
primeiro_digito = (resultado_digito_1*10) % 11;
primeiro_digito = primeiro_digito if primeiro_digito <= 9 else 0;
print(primeiro_digito);

dez_digitos = nove_digitos + str(primeiro_digito);
contador_regressivo_2 = 11;

resultado_digito_2 = 0;
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2;
    contador_regressivo_2 -= 1;
segundo_digito = (resultado_digito_2*10) % 11;
segundo_digito = segundo_digito if segundo_digito <= 9 else 0;
print(segundo_digito);

cpf_gerado_pelo_calculo = f"{nove_digitos}{primeiro_digito}{segundo_digito}";
if cpf_gerado_pelo_calculo == cpf:
    print(f"CPF VÁLIDO: {cpf_gerado_pelo_calculo}");
else:
    print(f"CPF INVÁLIDO: {cpf_gerado_pelo_calculo}");