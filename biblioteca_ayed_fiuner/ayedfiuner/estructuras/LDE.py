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
        """Devuelve el dato almacenado."""
        return self.__dato

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
        Inicia una lista originalmente vacía.
        Postcondición: La lista queda inicializada con cabeza en None, cola en None y tamaño 0.
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

    @property
    def tamanio(self):
        """Devuelve el tamaño."""
        return self.__tamanio

    def esta_vacia(self):
        """
        Determina si la lista no contiene elementos.
        Postcondición: Retorna True si el tamaño es 0, False en caso contrario.
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
        Precondición: dato es el elemento; posicion es un entero o None.
        Postcondición: Si posicion es None, agrega al final. Lanza IndexError si la posición es inválida.
        """
        if posicion is None:
            self.agregar_al_final(dato)
            return

        if posicion < 0 or posicion > self.__tamanio:
            raise IndexError("Posición inválida")

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

    def extraer(self, posicion=None):
        """
        Elimina y devuelve el ítem en la posición indicada.
        Precondición: posicion es un entero o None.
        Postcondición: Si posicion es None o -1, extrae el último. Lanza IndexError si la posición es inválida.
        """
        if self.esta_vacia():
            raise IndexError("Lista vacía")

        if posicion is None or posicion == -1:
            posicion = self.__tamanio - 1

        if posicion < 0 or posicion >= self.__tamanio:
            raise IndexError("Posición inválida")

        if posicion == 0:
            dato = self.__cabeza.dato
            self.__cabeza = self.__cabeza.siguiente
            if self.__cabeza: 
                self.__cabeza.anterior = None
            else: 
                self.__cola = None
        elif posicion == self.__tamanio - 1:
            dato = self.__cola.dato
            self.__cola = self.__cola.anterior
            if self.__cola: 
                self.__cola.siguiente = None
            else: 
                self.__cabeza = None
        else:
            actual = self.__cabeza
            for _ in range(posicion):
                actual = actual.siguiente
            dato = actual.dato
            actual.anterior.siguiente = actual.siguiente
            actual.siguiente.anterior = actual.anterior

        self.__tamanio -= 1
        return dato

    def copiar(self):
        """
        Realiza una copia de la lista elemento a elemento.
        Postcondición: Retorna una nueva instancia de ListaDobleEnlazada con los mismos datos.
        """
        nueva = ListaDobleEnlazada()
        actual = self.__cabeza
        while actual:
            nueva.agregar_al_final(actual.dato)
            actual = actual.siguiente
        return nueva

    def invertir(self):
        """
        Invierte el orden de los elementos de la lista actual.
        Postcondición: La lista actual queda invertida.
        """
        if self.esta_vacia() or self.__tamanio == 1:
            return None

        actual = self.__cabeza
        self.__cola = actual
        temp = None
        
        while actual:
            temp = actual.anterior
            actual.anterior = actual.siguiente
            actual.siguiente = temp
            actual = actual.anterior 
        
        if temp:
            self.__cabeza = temp.anterior
            
    def concatenar(self, otra_lista):
        """
        Recibe una lista y la une al final de la actual.
        Precondición: otra_lista debe ser una instancia de ListaDobleEnlazada.
        Postcondición: La lista original incorpora todos los elementos de otra_lista al final.
        """
        actual_otra = otra_lista.cabeza
        while actual_otra:
            self.agregar_al_final(actual_otra.dato)
            actual_otra = actual_otra.siguiente

    def __len__(self):
        """
        Devuelve la cantidad de elementos de la lista.
        Postcondición: Retorna un entero mayor o igual a 0.
        """
        return self.__tamanio

    def __add__(self, otra_lista):
        """
        Crea una nueva lista que es la suma de la actual y otra_lista.
        Precondición: otra_lista debe ser una instancia de ListaDobleEnlazada.
        Postcondición: Retorna una nueva lista sin modificar las originales.
        """
        nueva = self.copiar()
        nueva.concatenar(otra_lista)
        return nueva

    def __iter__(self):
        """
        Permite que la lista sea iterable.
        Postcondición: Produce un generador que recorre los datos desde la cabeza a la cola.
        """
        actual = self.__cabeza
        while actual:
            yield actual.dato
            actual = actual.siguiente