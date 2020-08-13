def torre (n, Fuente, Destino, Mitad):
    if n==1:
        print ("Mueve %i de la torre %s a la torre %s" %(n, Fuente, Destino))
    else:
        torre(n-1, Fuente, Mitad, Destino)
        print("Mueve %i de la torre %s a la torre %s" %(n,Fuente,Destino))
        torre(n-1, Mitad, Destino, Fuente)
        
torre(3, "A", "C", "B")

