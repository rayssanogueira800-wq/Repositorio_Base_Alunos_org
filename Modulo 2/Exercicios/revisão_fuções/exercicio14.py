def dividir_seguro(a, b):
    try:
        return a / b 
    except ZeroDivisionError:
        return None

print(dividir_seguro(10, 2))
print(dividir_seguro(8, 0))
print(dividir_seguro(9, 3))