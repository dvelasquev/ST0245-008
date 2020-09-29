import time
def lista_negativa(lista):
    listan = []
    for i in range (0,len(lista)):
        if lista[i] < 0:
            listan.append(lista[i])
    return listan

n = [-1,-4,-33,-5,-4,-5,-7,-8,-9,8,5,6,5,4,8,9,5,4,5,-5,-4,-4,-4,-14,-656565,-4,-8,8,5,7,5,7,6,5,4,5,4,9]
print (lista_negativa(n))

start_time = time.time() 
lista_negativa(n)
print("Tiempo --- %s seconds ---" % (time.time() - start_time))