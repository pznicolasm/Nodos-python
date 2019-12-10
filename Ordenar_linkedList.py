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
        if self.size  == 0:
            self.head = nuevo
            self.size+=1
        else:
            act=self.head
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
    
    
    def elimarValor(self,dato):
        if self.head.dato == dato:
            self.head=self.head.next
            self.size-=1
        else:
            cur = self.head
            pre=None
            while cur.next != None and cur.dato != dato:
                pre=cur
                cur=cur.next
            if cur.dato == dato:
                pre.next=cur.next
                self.size-=1
 
    
    def FindMenor(self):
        menor = self.head
        pre = self.head.next
        act = self.head.next.next
        while act != None:
            if menor.dato < pre.dato:
                pre=pre.next
                act = act.next
            else:
                menor=pre
                pre=pre.next
                act=act.next
        return menor

    def Ordeno(self):
        lista_ordenada=Linked_List()
        contador=0
        while self.size != contador:
            lista_ordenada.agregarFinal(self.FindMenor())
            self.elimarValor(self.FindMenor())
        print (lista_ordenada)

lista=Linked_List()
lista.agregarFinal(32)
lista.agregarFinal(11)
lista.agregarFinal(1)
lista.agregarFinal(115)
lista.agregarFinal(5)
lista.agregarFinal(87)
#lista.elimarValor(115)
#lista.FindMenor()
#lista.retornarDatoEnPos(1)
#lista.agregarPrimero(444)
#lista.eliminarUltimo()
#lista.imprimir()
lista.Ordeno()