class Nodo:
    def __init__(self, dato):
        """
        Inicia un nodo con un dato y referencias a sus nodos vecinos.
        Precondición: dato puede ser cualquier objeto comparable.
        Postcondición: Se crea un nodo con el dato y punteros anterior y siguiente en None.
        """
        self.__dato = dato
        self.__siguiente = None
        self.__anterior = None

    @property
    def dato(self):
        """Devuelve el dato almacenado en el nodo."""
        return self.__dato

    @dato.setter
    def dato(self, nuevo_dato):
        """Modifica el dato del nodo."""
        self.__dato = nuevo_dato

    @property
    def siguiente(self):
        """Devuelve el nodo siguiente."""
        return self.__siguiente

    @siguiente.setter
    def siguiente(self, nodo):
        """Establece el nodo siguiente."""
        self.__siguiente = nodo

    @property
    def anterior(self):
        """Devuelve el nodo anterior."""
        return self.__anterior

    @anterior.setter
    def anterior(self, nodo):
        """Establece el nodo anterior."""
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
        """Devuelve el atributo privado cabeza."""
        return self.__cabeza

    @property
    def cola(self):
        """Devuelve el atributo privado cola."""
        return self.__cola

    def esta_vacia(self):
        """
        Determina si la lista no contiene elementos.
        Postcondición: Retorna True si la lista está vacía, False en caso contrario.
        """
        return self.__tamanio == 0

    def agregar_al_inicio(self, dato):
        """
        Agrega un nuevo ítem al inicio de la lista.
        Precondición: dato es el elemento a agregar.
        Postcondición: El elemento se inserta en la cabeza.
        """
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.__cabeza = self.__cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.__cabeza
            self.__cabeza.anterior = nuevo_nodo
            self.__cabeza = nuevo_nodo
        self.__tamanio += 1

    def agregar_al_final(self, dato):
        """
        Agrega un nuevo ítem al final de la lista.
        Precondición: dato es el elemento a agregar.
        Postcondición: El elemento se inserta en la cola.
        """
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.__cabeza = self.__cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.__cola
            self.__cola.siguiente = nuevo_nodo
            self.__cola = nuevo_nodo
        self.__tamanio += 1

    def insertar(self, dato, posicion=None):
        """
        Agrega un nuevo ítem a la lista en la posición indicada.
        Precondición: dato es el elemento y posicion es un entero válido.
        Si posicion es None, se agrega al final.
        Postcondición: Inserta el nodo en la posición. Lanza Exception si es inválida.
        """

        if posicion is None:
            self.agregar_al_final(dato)
            return

        if posicion < 0 or posicion > self.__tamanio:
            raise Exception("Posicion Invalida")

        if posicion == 0:
            self.agregar_al_inicio(dato)
        elif posicion == self.__tamanio:
            self.agregar_al_final(dato)
        else:
            nuevo_nodo = Nodo(dato)
            actual = self.__cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            
            nuevo_nodo.anterior = actual.anterior
            nuevo_nodo.siguiente = actual
            actual.anterior.siguiente = nuevo_nodo
            actual.anterior = nuevo_nodo
            self.__tamanio += 1