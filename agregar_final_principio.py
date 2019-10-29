# Agregar al final y al principio:

class Nodo():
	def __init__(self, dato = None, nxt = None):
		self.dato = dato
		self.nxt = nxt
	
	def getdato(self):
		return self.dato
	def getnxt(self):
		return self.nxt
	def setdato(self, dato):
		self.dato = dato
	def setnxt(self, nxt):
		self.nxt = nxt

class LinkedList():
	
	def __init__(self, head = None):
			self.__head = head
	
	def setHead(self, head):
		self.__head = head
	
	def getHead(self):
		return self.__head

	def agregaralFinal(self, dato):
		nuevo = Nodo(dato, None)
		act = self.__head
		#Caso 1: si la lista esta vacia
		if (self.__head == None):
			self.__head = nuevo
			return True
		else:
			while(act.getnxt() != None):
				act = act.getnxt()
			act.setnxt(nuevo)
			return True

	def imprimirLista(self):
		act = self.__head
		while act.getnxt() != None:
			print(act.getdato())
			act = act.getnxt()
		print (act.getdato())
	
	def agregaralPrincipio(self, dato):
		nuevo = Nodo(dato, None)
		ant = self.__head
		self.__head = nuevo
		nuevo.setnxt(ant)
		return True

ll = LinkedList()
ll.agregaralFinal(34)
ll.agregaralFinal(24)
ll.agregaralPrincipio(56)
ll.agregaralPrincipio(56242423)

#(6)
#n4 = Nodo(30)
ll.imprimirLista()
