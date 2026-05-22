class MonticuloBinario:
    def __init__(self):
        """
        Postcondicion: Se crea una instancia de MonticuloBinario con una lista inicializada en [0] y tamaño 0.
        """
        self.listaMonticulo = [0]
        self.tamanoActual = 0

    def infiltArriba(self, i):
        """
        Precondición: el dato a ingresar i es un índice válido dentro de listaMonticulo.
        Postcondición: El elemento en la posición i se desplaza hacia arriba hasta que se restablece la propiedad de montículo.
        """
        while i // 2 > 0:
          if self.listaMonticulo[i] < self.listaMonticulo[i // 2]:
             tmp = self.listaMonticulo[i // 2]
             self.listaMonticulo[i // 2] = self.listaMonticulo[i]
             self.listaMonticulo[i] = tmp
          i = i // 2

    def insertar(self, k):
        """
        Precondición: k es un elemento comparable con los demás elementos del montículo.
        Postcondición: k se añade al montículo y se mantiene la propiedad de montículo. tamanoActual aumenta en 1.
        """
        self.listaMonticulo.append(k)
        self.tamanoActual = self.tamanoActual + 1
        self.infiltArriba(self.tamanoActual)

    def infiltAbajo(self, i):
        """
        Precondición: i es un índice válido dentro de listaMonticulo.
        Postcondición: El elemento en la posición i se desplaza hacia abajo hasta que se restablece la propiedad de montículo.
        """
        while (i * 2) <= self.tamanoActual:
            hm = self.hijoMin(i)
            if self.listaMonticulo[i] > self.listaMonticulo[hm]:
                tmp = self.listaMonticulo[i]
                self.listaMonticulo[i] = self.listaMonticulo[hm]
                self.listaMonticulo[hm] = tmp
            i = hm

    def hijoMin(self, i):
        """
        Precondición: El nodo en el índice i debe tener al menos un hijo.
        Postcondición: Devuelve el índice del hijo con el valor más bajo.
        """
        if i * 2 + 1 > self.tamanoActual:
            return i * 2
        else:
            if self.listaMonticulo[i*2] < self.listaMonticulo[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminarMin(self):
        """
        Precondición: El montículo no debe estar vacío.
        Postcondición: Se elimina y devuelve el elemento mínimo. El montículo se reestructura para mantener su propiedad.
        """
        valorSacado = self.listaMonticulo[1]
        self.listaMonticulo[1] = self.listaMonticulo[self.tamanoActual]
        self.tamanoActual = self.tamanoActual - 1
        self.listaMonticulo.pop()
        self.infiltAbajo(1)
        return valorSacado

    def construirMonticulo(self, unaLista):
        """
        Precondición: unaLista es una lista de elementos comparables.
        Postcondición: El atributo listaMonticulo se inicializa con los elementos de unaLista organizados como un montículo binario.
        """
        i = len(unaLista) // 2
        self.tamanoActual = len(unaLista)
        self.listaMonticulo = [0] + unaLista[:]
        while (i > 0):
            self.infiltAbajo(i)
            i = i - 1

# Ejemplo de ejecución
miMonticulo = MonticuloBinario()
miMonticulo.construirMonticulo([9,5,6,2,3])

print(miMonticulo.eliminarMin())
print(miMonticulo.eliminarMin())
print(miMonticulo.eliminarMin())
print(miMonticulo.eliminarMin())
print(miMonticulo.eliminarMin())