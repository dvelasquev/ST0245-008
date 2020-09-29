A = [96, 65, 29, 25, 67, 97, 77, 42, 25, 89, 84, 76, 57, 49, 39, 77, 65, 6, 84, 58, 46, 78, 9, 4, 94, 39, 96, 10, 10, 19, 80, 20, 82, 68, 77, 81, 0, 31, 33, 42, 12, 86, 77, 30, 83, 87, 38, 40, 16, 45, 3, 42, 67, 65, 92, 43, 71, 13, 26, 13, 1, 94, 78, 20, 11, 59, 6, 12, 18, 51, 43, 19, 84, 29, 36, 14, 8, 83, 51, 75, 56, 84, 5, 32, 4, 45, 22, 42, 55, 28, 46, 4, 77, 80, 96, 81, 91, 55, 15, 98]
B = [23, 39, 57, 40, 29, 23, 10, 9, 50, 11, 18, 55, 4, 56, 50, 39, 57, 44, 39, 34, 41, 23, 4, 37, 16, 25, 19, 9, 31, 1, 0, 48, 8, 52, 54, 12, 36, 25, 50, 57, 1, 30, 30, 24, 58, 8, 13, 52, 6, 36, 41, 55, 48, 35, 12, 19, 41, 3, 17, 26]
def quick_sort(lista):
    izquierda = []
    derecha = []
    centro = [] # Siempre sera una lista de un solo elemnto
    
    if len(lista)>1:
        pivote = lista[len(lista)-1]
        for i in lista:
            if i<pivote:
                izquierda.append(i)
            elif i  == pivote:
                centro.append(i)
            else:
                derecha.append(i)
        return quick_sort(izquierda) + centro + quick_sort(derecha)
    else:
        return lista
print("Lista A ordenada: ")
print(quick_sort(A)) #Lista A ordenada
print("Lista B ordenada: ")
print(quick_sort(B)) #Lista B ordenada

C = A + B 
print("Lista C ordenada: ")
print (quick_sort(C)) #Lista C Ordenada

