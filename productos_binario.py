class Producto:

    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Nodo:

    def __init__(self, dato=None):
        self.izq = None
        self.der = None
        self.dato = dato

    def insertar(self, dato):
        if self.dato:
            if dato.precio < self.dato.precio: #el precio es de la clase dato, ese dato es un objeto que tiene un nombre y un precio
                if self.izq is None:
                    self.izq = Nodo(dato)
                else:
                    self.izq.insertar(dato)
            elif dato.precio > self.dato.precio:
                if self.der is None:
                    self.der = Nodo(dato)
                else:
                    self.der.insertar(dato)
        else:
            self.dato = dato

    def imprimirArbol(self):
        if self.izq:
            self.izq.imprimirArbol()
        print( self.dato.nombre),
        if self.der:
            self.der.imprimirArbol()

root = Nodo()
a=Producto("arroz",40)
b=Producto("vino",120)
c=Producto("pan",60)
d=Producto("queso",140)
e=Producto("fideos",50)
f=Producto("agua",30)
g=Producto("cerveza",75)

l = [a,b,c,d,e,f,g]


for i in l:
    root.insertar(i)

root.imprimirArbol()

#Esto imprime el nombre de los productos ordenados por su precio 