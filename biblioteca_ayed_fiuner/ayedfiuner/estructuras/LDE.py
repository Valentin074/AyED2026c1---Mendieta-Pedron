class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__siguiente = None
        self.__anterior = None

class ListaDobleEnlazada:
    def __init__(self):
        self.__cabeza = None
        self.__cola = None
        self.__tamanio = 0

    def agregar_al_inicio(self,dato):
        nuevo_nodo = Nodo(dato)
        if self.tamanio == 0
            self.__cabeza = nuevo_nodo
            self.__cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamanio += 1 

    def insertar(self, dato, posicion):
        if posicion < 0 or posicion > self.tamanio:
            raise Exception("Posicion Invalida")
        elif posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.tamanio:
            self.agregar_al_final(dato)



        