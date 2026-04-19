class Nodo:
    def __init__(self, dato):

        """
        Inicia un nodo con un dato y referencias a sus nodos vecinos.
        Precondición: dato puede ser cualquier objeto comparable.
        Postcondición: Se crea un nodo con el dato y punteros en None.
        """

        self.__dato = dato
        self.__siguiente = None
        self.__anterior = None

    @property
    def dato(self):
        return self.__dato
    @dato.setter
    def dato(self, nuevo_dato):
        self.__dato = nuevo_dato

    @property
    def siguiente(self):
        return self.__siguiente
    @siguiente.setter
    def siguiente(self, nodo):
        self.__siguiente = nodo
    
    @property
    def anterior(self):
        return self.__anterior
    @anterior.setter
    def anterior(self, nodo):
        self.__anterior = nodo

class ListaDobleEnlazada:
    def __init__(self):

        """
        Inicia una lista doblemente enlazada vacía.
        Postcondición: La lista queda creada con cabeza y cola en None, y tamaño 0.
        """

        self.__cabeza = None
        self.__cola = None
        self.__tamanio = 0

    @property
    def cabeza(self):
        return self.__cabeza
    
    @property
    def cola(self):
        return self.__cola