a = input("Ingrese una número\n")
b = " "
def Capicua(a,b):
    b = a[::-1]
    if a == b:
        return a,"es un número capicúa"
    else:
        return a,"no es un número capicúa"
print(Capicua(a,b))      