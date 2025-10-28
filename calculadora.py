def suma(a, b):
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
    print("divide(6,2) =", divide(6, 2))
