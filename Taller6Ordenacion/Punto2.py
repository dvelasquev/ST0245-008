Lista = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,6,6,6,7,7,7,8,9]
Vacia = []
for i in Lista:             #El for mira todos los elementos
    if i not in Vacia:      #El if busca todos los duplicados
        Vacia.append(i)     #El append añade los elementos solo si no están duplicados
print(Vacia)