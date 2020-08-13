from functools import lru_cache #least recently used cache, me añade la memorización en una línea
@lru_cache(maxsize = 1000)
#Revisar que el input sea un número positivo
def fibonacci(n):
    if type(n) != int:
     raise TypeError ("n debe ser un número positivo")
    if n < 1:
        raise TypeError ("n debe ser un número positivo")

#Calcular el enésimo termino 
    if n==1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci (n-1) + fibonacci (n-2)

for n in range (1,101):
    print(fibonacci(n))
