a = int(input("Ingrese un número\n"))
b = int(input("Ingrese otro número\n"))
c = 1
if b > a:
    c = a
    a = b
    b = c
def mcd(a,b):
    if a % b == 0:
        return b
    else:
        a = b
        b = a % b
print("El M.C.D es: ",mcd(a,b))