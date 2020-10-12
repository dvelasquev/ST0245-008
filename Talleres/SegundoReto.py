'''
    Solución al reto Amazon correspondiente al parcial 2
    Diego Velásquez Varela

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, he):
        self.he = he
    def length(self):
        current = self.he
        if current is not None:
            count = 1
            while current.next is not None:
                count += 1
                current = current.next
            return count
        else:
            return 0
    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = head.he
            head.he = new_node
        else:
            current = head.he
            k = 1
            while current.next is not None and k < position:
                current = current.next
                k += 1
            new_node.next = current.next
            current.next = new_node   

    def Iter(self,k):
        if k >= self.length():
            k=k%self.length()
        
        j = 1
        while j <= k:
            current = self.he
            while current.next.next is not None:
                current = current.next
            current.next.next = self.he
            self.he = current.next
            current.next = None
            j+=1

    def lalista(self):
        current = head.he
        while current is not None:
            print(current.data, end = '')
            current = current.next
            print()
head = SinglyLinkedList(Node(1))
for j in range (2,6):
    head.insert(j,j-1)

print('La lista inicial es: ')
head.lalista()
head.Iter(994)
print("Lista después de ser rotada 994 veces: ")
head.lalista()

'''
Este mismo ejercicio, puede simplificarse usando rotate(), un método de la clase Deque que se nos
fue explicada en clase
El método rotate () nos va rotar la secuencia presente en el objeto deque "n" veces.
- Si no se pasa ningún parametro, n tiene valor predeterminado de 1
- Si n es negativo, la rotación es de derecha a izquierda
- si n es positivo, la rotación es de izquierda a derecha

El método no devuelve una 'Copia' del deque que tiene la nueva secuencia.
La rotación se aplica al contenido/interior del mismo objeto deque

'''
import collections
#Creamos un objeto vacío deque
Objeto_Deque = collections.deque()
#Agregamos los elementos a deque de izquierda a derecha
Objeto_Deque.append(1)
Objeto_Deque.append(2)
Objeto_Deque.append(3)
Objeto_Deque.append(4)
Objeto_Deque.append(5)
#Imprimimos el contenido de deque
print("Deque sin ninguna rotación: ")
print(Objeto_Deque)

Objeto_Deque.rotate(994)
print ("Deque rotado positivamente 994 veces ")
print(Objeto_Deque)

'''
Ahora, para rotar el objeto Deque un número negativo de 
veces, y con una tupla
'''
secuencia = (1,2,3,4,5)
secuenciaDeque = collections.deque(secuencia)
print("Deque sin ningúna rotación")
print(secuenciaDeque)
secuenciaDeque.rotate(-994)
print("Deque con 994 rotaciones, pero esta vez negativas: ")
print(secuenciaDeque)

'''
Vemos como la primera implementación, es un tipo de lista enlazada que es unidireccional,
esto es, que puede atravesarse/recorrerse en una sola dirección, desde la cabeza hasta el último nodo o cola,
por otra parte Deque (o cola doblemente terminada), también es una estructura de datos lineal, pero permite
insertar y eliminar elementos por ambos extremos, en si, es un mecanismo que une en una única estructura
la funcionalidad Last in First Out y la First In First Out, en resumen, las pilas y colas se pueden implementar
un poco más sencillo con una deque (que además tiene la ventaja de incluirse entre los métodos que ofrece python pre-establecidos)
'''

'''
Para la solución de este reto, utilicé los siguientes apoyos bibliograficos.
https://www.youtube.com/watch?v=FSsriWQ0qYE
https://pythontic.com/containers/deque/rotate
https://pccito.ugr.es/~gustavo/stl/deque.html
Donald Knuth. The Art of Computer Programming, Volume 1: Fundamental Algorithms, 
Third Edition. Addison-Wesley, 1997. ISBN 0-201-89683-4. Section 2.2.1: Stacks, Queues, and Deques, pp. 238–243.
https://www.geeksforgeeks.org/implement-a-stack-using-singly-linked-list/
'''