class Nodo():
    def __init__(self,dato=None):
        self.dato=dato
        self.next=None
    
    def __str__(self):
        return str(self.dato)

class Linked_List():
    def __init__(self):
        self.head=None
        self.size=0

    def __str__(self):
        return str(self.head.dato)

    def agregarFinal(self,dato):
        nuevo=Nodo(dato)
        act=self.head
        if self.size  == 0:
            self.head = nuevo
            self.size+=1
        else:
            while act.next != None:
                act = act.next
            act.next= nuevo
            self.size+=1
    
    def imprimir(self):
        if self.size == 0:
            print ("Esta vacia")
        else:
            act=self.head
            while act != None:
                print (act.dato)
                act = act.next

    def agregarPrimero(self,dato):
        nuevo=Nodo(dato)
        if self.size == 0:
            self.head = nuevo
            self.head.next = None
        else:
            aux=self.head
            self.head=nuevo
            nuevo.next=aux

    def eliminarPrimero(self):
        self.head=self.head.next

    def eliminarUltimo(self):
        act=self.head
        pre=self.head
        while act.next != None:
            pre=act
            act=act.next
        pre.next=None
    
    def retornarDatoEnPos(self,posicion):
        indice=0
        act=self.head
        while act != None and posicion != indice:
            act=act.next
            indice+=1
        if act is posicion:
            print (act.dato)

    def retornarUltimo(self):
        act=self.head
        while act.next != None:
            act=act.next
        print (act.dato)



lista=Linked_List()
"""lista.agregarFinal(32)
lista.agregarFinal(11)
lista.agregarFinal(115)
lista.agregarFinal(87)
#lista.retornarDatoEnPos(1)
#lista.agregarPrimero(444)
#lista.eliminarUltimo()
#lista.imprimir()"""

class Pila():
    def __init__(self):
        self.items=Linked_List()
        self.size=0
    
    def __str__(self):
        return (str(self.items))

    def Push(self,dato):
        self.items.agregarFinal(dato)
        self.size+=1
    
    def Pop(self):
        self.items.eliminarUltimo()
        self.size-=1

    def Imprimir(self):
        self.items.imprimir()

    def Reversed(self):
        pila_reverse=Pila()
        contador=0
        while self.size != contador:
            pila_reverse.Push(self.items.retornarUltimo())
            self.Pop()

            

lista_pila=Pila()
lista_pila.Push("o")
lista_pila.Push("t")
lista_pila.Push("u")
lista_pila.Push("p")
print ("La lista normal: ", lista_pila.Imprimir())
print ("La lista al reves: " , lista_pila.Reversed())

