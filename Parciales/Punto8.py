#Mi tarjeta de identidad es 1001421065, por lo tanto tomo el 65 para la cuenta atrás
def printN(n):
    if n == 0:
        return
    else:
        print(n)
        printN(n-1)
    
printN(65)
