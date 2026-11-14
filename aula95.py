# raise - lançando exceções em Python

def nao_aceito_zero(b):
    if b == 0:
        raise ZeroDivisionError("O divisor não pode ser zero.")
    return True

def deve_ser_int_float(a, b):
    if not isinstance(b, (int, float)) or not isinstance(a, (int, float)):
        raise TypeError("Os argumentos devem ser números.")
    return True

def dividir(a, b):
    deve_ser_int_float(a, b)
    nao_aceito_zero(b)
    return a / b

print(dividir(10, 2))  # Saída: 5.0
print(dividir(10, 0))  # Lança ValueError: O divisor não