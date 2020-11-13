#Implementacion del postorden partiendo de preorden e inorden conocidos
def postorden(preorden, inorden):
    if preorden == "" or inorden == "":
        return ""
    if len(preorden) == 1 or len(inorden) == 1:
        return preorden or inorden
    PostOrden = ""
    Ino_izq = ""
    Pre_izq = ""
    Ino_der = ""
    Pre_der = ""
    aux = 0
    while inorden[aux] != preorden[0]:
        Ino_izq = Ino_izq + inorden[aux]
        aux+=1
    aux+=1
    while aux<len(inorden):
        Ino_der = Ino_der + inorden[aux]
        aux+=1
    aux=0
    for i in preorden:
        if i in Ino_izq:
            Pre_izq = Pre_izq + i
        if i in Ino_der:
            Pre_der = Pre_der + i
    PostOrden = PostOrden+postorden(Pre_izq, Ino_izq)+postorden(Pre_der, Ino_der)+preorden[0]
    return PostOrden
print(postorden("GEAIBMCLDFKJH", "IABEGLDCFMKHJ"))

#Output = IBAEDLFCHJKMG