a = int(input("Ingrese la base\n"))
b = int(input("Ingrese el índice\n"))
def potencia(a,b):
    if b == 0:
        return 1
    else:
        if b == 1:
            return a
        else:
            return a * potencia(a,b-1)
print("El valor dela potencia es: ",potencia(a,b))