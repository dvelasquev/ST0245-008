'''
Diego Velásquez Varela
Para el reto 3 nos encontramos con una implementación dentro de un arbol binario,
en el cual pueden realizarse operaciones como insertar nodos, impremir en pre/in/post orden,
así como también busqueda y eliminado de datos. Lo anterior puede probarse desde el main :) 
'''
import os

class node():
    def __init__(self, dato):
        self.left = None
        self.right = None
        self.dato = dato

class arbol():
    def __init__(self):
        self.root = None
        
    def insert(self, a, dato):
        assert self.buscar(dato,a) == None, "Dato ya existente"
        if a == None:
            a = node(dato)
        else:
            d = a.dato
            if dato < d:
                a.left = self.insert(a.left, dato)
            else:
                a.right = self.insert(a.right, dato)
        return a

    def inorder(self, a):
        if a == None:
            return None
        else:
            self.inorder(a.left)
            print(a.dato)
            self.inorder(a.right)

    def preorder(self, a):
        if a == None:
            return None
        else:
            print(a.dato)
            self.preorder(a.left)
            self.preorder(a.right)

    def postorder(self, a):
        if a == None:
            return None
        else:
            self.postorder(a.left)
            self.postorder(a.right)
            print(a.dato)

    def buscar(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a.dato
            else:
                if dato < a.dato:
                    return self.buscar(dato, a.left)
                else:
                    return self.buscar(dato, a.right)

    def Acceso(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a
            else:
                if dato < a.dato:
                    return self.Acceso(dato, a.left)
                else:
                    return self.Acceso(dato, a.right)

    def MinNodo (self, node):
        act = node
        while (act.left is not None):
            act = act.left
        return act

    def Borrado (self,dato,a):
        if a == None:
            return a
        if (dato < a.dato):
            a.right = self.Borrado(a.left, dato)
        elif (dato > a.dato):
            a.right = self.Borrado(a.right, dato)
        else:
            if a.left == None:
                temp = a.right
                a = None
                return temp
            elif a.right == None:
                temp = a.left
                a = None
                return temp
            temp = self.MinNodo(a.right)
            a.dato = temp.dato
            a.right = self.Borrado(a.right, temp.dato)
        return a

tree = arbol()

while True:
    os.system("cls")
    print("Arbol ABB")
    opc = input("\n1.-Insertar nodo \n2.-Inorden \n3.-Preorden \n4.-Postorden \n5.-Buscar \n6.-Borrar Dato \n7.-Salir \n\nElige una opcion -> ")

    if opc == '1':
        nodo = input("\nIngresa el nodo -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            tree.root = tree.insert(tree.root, nodo)
        else:
            print("\nIngresa solo digitos...")
    elif opc == '2':
        if tree.root == None:
            print("Vacio")
        else:
            tree.inorder(tree.root)
    elif opc == '3':
        if tree.root == None:
            print("Vacio")
        else:
            tree.preorder(tree.root)
    elif opc == '4':
        if tree.root == None:
            print("Vacio")
        else:
            tree.postorder(tree.root)
    elif opc == '5':
        nodo = input("\nIngresa el nodo a buscar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if tree.buscar(nodo, tree.root) == None:
                print("\nNodo no encontrado...")
            else:
                print("\nNodo encontrado -> ",tree.buscar(nodo, tree.root), " si existe...")
        else:
            print("\nIngresa solo digitos...")        
    elif opc == '6':
        digito = int(input("\n Ingrese el digito que quiere borrar\n"))
        tree.Borrado(tree.root,digito)
      
    elif opc == '7':
        print("\nElegiste salir...\n")
        os.system("pause")
        break
    else:
        print("\nElige una opcion correcta...")
    print()
    os.system("pause")

print()

'''
Se agregó el assert en caso de que cause problemas si el usuario pone números repetidos
La implementación no tiene ningún inconveniente a la hora de trabajar con arboles binarios
'''
