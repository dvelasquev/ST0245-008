'''
Para la solución de este punto utilizo el código del reto3, 
correspondiente a realizar operaciones en un arbol binario,
en este caso, añado la función de altura. Sin embargo para simplificarlo un poco eliminamos el menú
de la consola
'''
class Nodo:
    
    def __init__(self,dato):
        self.dato=dato
        self.Hijo_Izquierdo=None
        self.Hijo_Derecho=None
        
class Arbol:
    def __init__(self):
        self.raiz= None
        
    def Raíz(self):
        return self.raiz
    
    def aggvalor(self,val):
        if(self.raiz==None):
            self.raiz = Nodo(val)
        else:
            self.N_Nodo(val,self.raiz)
    
    def N_Nodo(self, val, nodo):
        if(val<nodo.dato):
            if(nodo.Hijo_Izquierdo!=None):
                self.N_Nodo(val,nodo.Hijo_Izquierdo)
            else:
                nodo.Hijo_Izquierdo = Nodo(val)
        else:
            if(nodo.Hijo_Derecho!=None):
                self.N_Nodo(val,nodo.Hijo_Derecho)
            else:
                nodo.Hijo_Derecho = Nodo(val)
    
    def inorder(self,root):
        if root ==None:
            return
        self.inorder(root.Hijo_Izquierdo)
        print(root.dato)
        self.inorder(root.Hijo_Derecho)
  
    def altura(self,nodo):
        h=0
        if nodo == None:
            return 0
        if nodo.Hijo_Izquierdo!=None:
            h = max(h,self.altura(nodo.Hijo_Izquierdo))
        if nodo.Hijo_Derecho != None:
            h = max(h,self.altura(nodo.Hijo_Derecho))
        h+=1
        return h


tree = Arbol()

altura = tree.altura(tree.Raíz())
print("altura:",altura)
    
