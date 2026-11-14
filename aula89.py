# dir, hasattr e getattr em Python

string = "Kalliana"
metodo = "upper"

if hasattr(string, metodo):
    print(getattr(string, metodo)())

