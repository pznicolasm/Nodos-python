class Nodo():                #Instancia
	def __init__(self, dato = None,next = None): #variable por defecto    
  		self.__dato = dato
  		self.__next = next

# El tipo de dato de next es "nodo" y el primero arranca en "None"
	
	def getDato(self):
		return self.__dato
	def getNext(self):
		return self.__next
	def setDato(self, dato):
		self.__dato = dato
	def setNext(self, next):
		self.__next = next

#Instanciamos, creo 3 nodos con instancia de la clase nodo. "representaciones fisicas de la clase"
#Le mando solo un parametro, el dato. el otro ya queda en NONE
nodo1 = Nodo (1)
nodo2 = Nodo (2)
nodo3 = Nodo (3)
#Al next de cada valor, se le asigna el siguiente. pasa a apuntar al siguiente.
nodo1.setNext (nodo2)
nodo2.setNext (nodo3)
#NODO1 TIPO DE DATO = INSTANCIA DE LA CLASE NODO
#Imprimo el data del nodo1
print(nodo1.getDato())
#Imprimo una instancia de clase nodo. y luego getDato, me da el dato del nodo 2
#Nodo1 es una instancia de la clase Nodo
print(nodo1.getNext().getDato())
#pido el next del next y luego la data.. me va a devolver el Nodo3
print(nodo1.getNext().getNext().getDato())

#Le cambio el dato al nodo 3
nodo1.getNext().getNext().setDato(400)

#Ahora creo la clase linkedlist, que lleva como parametro solo HEAD.
#Son nodos que tienen como siguiente a otro nodo

class Linkedlist():
	def __init__(self, head = None):
		self.__head = head

	def getHead(self):
		return self.__head

	def setHead(self, head):
		self.__head = head

	def agregarFinal(self, data):
		nuevo = Nodo(data)
		#CASO 1: LA LISTA ESTA VACIA
		if self.__head == None:
			self.__head = nuevo
			return True                   #Me corta la ejecucuon el true
		#CASO 2: LA LISTA NO ESTA VACIA
		act = self.__head                 #Nodo de avance
		while act.getNext() != None: #getNext es de la instancia node pero act de de clase nodo
			act = act.getNext()
			#Cuando termine el while, act va a tener un none, entonces ahi le asignamos el nuevo con el setnext
		act.setNext(nuevo)
		return True

	def imprimirLista(self):
		print("Imprimir lista")
		act = self.__head
		while act.getNext() != None:
			print(act.getDato())
			act = act.getNext()
		print(act.getDato())


	def recorrerLista(self):
		print("recorrerLista")
		act = self.__head
		count = 0
		while act != None:
			act = act.getNext()
			print(count)
			count = count + 1
		print(count)

ll = Linkedlist()
ll.agregarFinal(100)
ll.agregarFinal(200)
ll.agregarFinal(300)
ll.agregarFinal(400)
ll.agregarFinal(500)

ll.imprimirLista()
ll.recorrerLista()

print(nodo3.getDato(), "aca se ve el cambio en el dato del nodo3")

#EN la clase del 8/10 dieron la funcion para agregar al principio y al final
