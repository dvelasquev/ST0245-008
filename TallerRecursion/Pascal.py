n = int(input("Ingrese el número de filas: \n"))
def pascal(n):
    if n == 0:
        return []
    elif n == 1:
        return [1]
    else:
        nuevaFila = [1]
        ultimaFila = pascal(n-1)
        for i in range(len(ultimaFila)-1):
            nuevaFila.append(nuevaFila[i] + ultimaFila[i+1])
        nuevaFila += [1]
    return nuevaFila
print("El triángulo resultante es: \n",pascal(n))