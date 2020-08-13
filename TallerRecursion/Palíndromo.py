a = input("Ingrese una palabra\n")
b = " "
def palindromo(a,b):
    b = a[::-1]
    if a == b:
        return "La palabra es un palíndromo"
    else:
        return "La palabra no es un palíndromo"
print(palindromo(a,b))      