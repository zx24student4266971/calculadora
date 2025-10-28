def suma(a, b):
    """
    Suma con validación básica y conversión de strings numéricos.
    """
    if a is None or b is None:
        raise ValueError("Los operandos no pueden ser None")
    try:
        if isinstance(a, str):
            a = float(a) if '.' in a else int(a)
        if isinstance(b, str):
            b = float(b) if '.' in b else int(b)
    except Exception:
        raise ValueError("No se pudo convertir operandos a número")
    return a + b

def resta(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division por cero")
    return a / b

if __name__ == "__main__":
    print("suma(2,3) =", suma(2, 3))
    print("suma('2','3') =", suma('2', '3'))
    print("divide(6,2) =", divide(6, 2))
