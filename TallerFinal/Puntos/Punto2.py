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
    def promedio(self):
        suma= self.pilaaa[0]
        for i in range (len(self.pilaaa)-1):
            suma = suma+self.pilaaa[i+1]
            prom = suma/len(self.pilaaa)
            return prom

pilapromedio = Pila()
for i in range(6):
    pilapromedio.apilar(i)
print("Pila: ", pilapromedio)
pila_auxiliar= pilapromedio.promedio()
print("Promedio: ", pila_auxiliar)
