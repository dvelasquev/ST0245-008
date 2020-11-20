class Alumno:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
    def __str__(self):
       return self.nombre+' - '+str(self.edad)+' años :'+str(self.nota)
class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None

primero = None
L_Alumnos = [Alumno('Alex', 30, 8.9), Alumno('Pepe', 27, 3.7)]
for alumno in L_Alumnos:
    nodo = Nodo(alumno)
    nodo.siguiente = primero
    primero = nodo
    print(nodo.datos)
n = primero


