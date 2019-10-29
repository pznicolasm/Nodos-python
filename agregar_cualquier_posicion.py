# 1) Agregar en cualquier posicion, pasada por parametro. necesito sabes posicion -> longitud list -> recorrer list -> retornar un num
# 2) Desarrollar una funcion que retorne y borre de la lista (pop) de una posicion random
# para el punto 2 ; funcion "obtener longitud de lista", "generar numero random dentro de un rango (import random)", "borrar pos dada por parametro"
 
class Nodo ():
    def __init__ (self, dato = None, netx = None):
        self.dato = dato
        self.next = next
    def getDato (self):
        return self.dato
    def getNext (self):
        return self.next
    def setDato (self, dato):
        self.dato = dato
    def setNext (self, next):
        self.next = next

class LinkedList ():                      #Lista enlazada de nodos
    def __init__ (self, head = None):
        self.head = head
    def getHead (self):
        return self.head
    def setHead (self, head):
        self.head = head
    
    def recorreLista (self):     #Longitud de la lista
        "Recorre lista"
        act = self.head
        count = 0
        while act != None:
            act = act.getNext()
            count = count + 1
        return count              #Len de lista

    def imprimirLista (self):
        "Imprime lista"
        act = self.head
        while act.getNext != None:
            print(act.getDato())
            act = act.getNext()
        print(act.getDato())

    def agregarCualquierPos (self, dato, pos):
        nuevo = Nodo (dato)
        act = self.head
        count = self.recorreLista()        #Me devuelve el count por que en la funcion esta como retunr! ***importante el uso del RETURN!***
        #CASO 1: LISTA VACIA, AGREGA AL PRINCIPIO:
        if self.head == None:
            self.head = nuevo
            return True
        #CASO 2: POS > AL LEN DE LISTA. AGREGA AL FINAL:
        if pos >= count:
            act = act.getNext()
            act = act.setNext()
            return True
        #CASO 3: A LA POSICION:
        i = 1                          # i empieza en 1 por que el len de lista no toma 0
        act = self.head
        while (act.sig != None) or (i != pos):
            i = i + 1
            ant = act                  #Necesito tener un ant que vaya guardando la posicioin anterior
            act = act.getNext()
        act.getNext = nuevo
        nuevo.getNext = act
