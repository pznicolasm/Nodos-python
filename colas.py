class Nodo():
    def __init__(self, dato=None, next = None):
        self.dato=dato
        self.next=next
    
    def __str__(self):
        return str(self.dato)

class LinkedList():
    def __init__(self,head=None):
        self.head=head
        self.size=0

    def __str__(self):
        if self.size == 0:
            print ("esta vacia")
        else:
            act=self.head
            while act != None:
                print (act.dato)
                act=act.next
    
class Queue():
    def __init__(self):
        self.first= self.last=None
        self.size=0

    def __str__(self):
        if self.first == None:
            print ("esta vacia")
        else:
            act=self.first
            while act != None:
                try:
                    print(act.dato)
                    act=act.next
                except:
                    print("listo")
                    break

    def isEmpty(self):
        return self.first == None
    
    def EnQueue(self,valor):
        aux=Nodo(valor)

        if self.last ==None:
            self.first = self.last = aux
            return
        self.last.next=aux
        self.last=aux
        self.size+=1

    def DeQueue(self):
        if self.isEmpty():
            return
        aux=self.first
        self.first = aux.next

        if self.first == None:
            self.last = None
        self.size -=1
        return str(aux.dato)

q = Queue()
q.EnQueue(10)
q.EnQueue(20)
q.EnQueue(30)
q.DeQueue()
q.DeQueue()
print(q)

""" Tiene un error de tipo pero funciona el resto 
Traceback (most recent call last):
  File "/home/pablo/Documentos/x1Desarrollos/Test/cola.py", line 71, in <module>
    print(q)
TypeError: __str__ returned non-string (type NoneType)
"""



