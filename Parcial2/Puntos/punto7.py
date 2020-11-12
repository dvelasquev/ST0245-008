class Pila: #Implementacion de la clase Pila con las funciones
    def __init__(self):
        self.pilaaa = []
    def __str__(self):
        return str(self.pilaaa)
    def vacia(self): #Comprobar si es vacía
        return len(self.pilaaa) == 0
    def apilar(self, data): #Agregar un elemento
        self.pilaaa.append(data)
    def desapilar(self): #Eliminar un elemento
        assert not self.vacia()
        return self.pilaaa.pop()
    def Invertida(self): #Lo que nos pide el punto, invertir la pila
        Inversa = Pila()
        for i in range(1, len(self.pilaaa)):
            Inversa.apilar(self.pilaaa[-i])
        Inversa.apilar(self.pilaaa[0])
        for i in range(len(self.pilaaa)):
            self.desapilar()
        return Inversa

pilaprueba = Pila()
for i in range(10):
        pilaprueba.apilar(i)
print('Pila de las posiciones de 0-10: ',pilaprueba)
pila_auxiliar = pilaprueba.Invertida()
print('Pila con posiciones invertidas',pila_auxiliar)
print('La pila nula es ', pilaprueba)
