def shell_Sort(lista):
    cont = 1
    cont_Sublista = len(lista)//2
    while cont_Sublista > 0:
        for psiInicio in range(cont_Sublista):
            brecha_ord_insercion(lista,psiInicio,cont_Sublista)
        
        cont_Sublista = cont_Sublista//2
    return lista
    
def brecha_ord_insercion(lista, inicio, brecha):
    for i in range(inicio + brecha,len(lista), brecha):
        valor_actual = lista[i]
        posicion = i
        while posicion >= brecha and lista[posicion-brecha] > valor_actual:
            lista[posicion] = lista[posicion-brecha]
            posicion = posicion-brecha
        lista[posicion]=valor_actual

lista = [8,43,17,6,40,16,18,97,11,7]
print(shell_Sort(lista))