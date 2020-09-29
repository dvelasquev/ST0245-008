Lista = [4,7,11,4,9,5,11,7,3,5]
Vacia = []
for i in Lista:         #El for mira todos los elementos
    if i not in Vacia:  #El if busca todos los duplicados
        Vacia.append(i) #El append añade los elementos solo si no están duplicados
print(Vacia)
