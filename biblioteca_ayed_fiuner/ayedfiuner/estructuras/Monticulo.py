# -*- coding: utf-8 -*-

class MonticuloBinarioMinimo:
    def __init__(self):
        """
        Postcondición: Crea un montículo binario vacío con un elemento dummy en el índice 0.
        """
        self.lista_monticulo = [0]
        self.tamano_actual = 0

    def esta_vacio(self):
        """
        Postcondición: Devuelve True si el montículo no tiene elementos, False en caso contrario.
        """
        return self.tamano_actual == 0

    def infilt_arriba(self, i):
        """
        Precondición: i es un índice válido dentro del montículo (1 <= i <= tamano_actual).
        Postcondición: Desplaza el elemento en el índice i hacia arriba hasta restaurar la propiedad de montículo mínimo.
        """
        if not (1 <= i <= self.tamano_actual):
            raise IndexError("Índice fuera de rango para infiltración hacia arriba.")

        while i // 2 > 0:
            if self.lista_monticulo[i] < self.lista_monticulo[i // 2]:
                self.lista_monticulo[i // 2], self.lista_monticulo[i] = self.lista_monticulo[i], self.lista_monticulo[i // 2]
            i = i // 2

    def insertar(self, k):
        """
        Precondición: k es un elemento comparable con los que ya existen en el montículo.
        Postcondición: Agrega k al montículo manteniendo la propiedad de orden.
        """
        if k is None:
            raise ValueError("No se pueden insertar elementos nulos (None).")
        self.lista_monticulo.append(k)
        self.tamano_actual += 1
        self.infilt_arriba(self.tamano_actual)

    def infilt_abajo(self, i):
        """
        Precondición: i es un índice válido dentro del montículo (1 <= i <= tamano_actual).
        Postcondición: Desplaza el elemento en el índice i hacia abajo hasta restaurar la propiedad de montículo mínimo.
        """
        if not (1 <= i <= self.tamano_actual):
            raise IndexError("Índice fuera de rango para infiltración hacia abajo.")

        while (i * 2) <= self.tamano_actual:
            hm = self.hijo_min(i)
            if self.lista_monticulo[i] > self.lista_monticulo[hm]:
                self.lista_monticulo[i], self.lista_monticulo[hm] = self.lista_monticulo[hm], self.lista_monticulo[i]
            i = hm

    def hijo_min(self, i):
        """
        Precondición: El nodo en la posición i debe tener al menos un hijo y ser un índice válido.
        Postcondición: Devuelve el índice del hijo con el menor valor.
        """
        if not (1 <= i <= self.tamano_actual):
            raise IndexError("Índice fuera de rango para buscar hijo mínimo.")

        if i * 2 + 1 > self.tamano_actual:
            return i * 2
        else:
            if self.lista_monticulo[i * 2] < self.lista_monticulo[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def eliminar_min(self):
        """
        Precondición: El montículo no debe estar vacío.
        Postcondición: Remueve y devuelve el elemento mínimo del montículo.
        """
        if self.esta_vacio():
            raise IndexError("No se puede eliminar de un montículo vacío.")
        valor_sacado = self.lista_monticulo[1]
        self.lista_monticulo[1] = self.lista_monticulo[self.tamano_actual]
        self.tamano_actual -= 1
        self.lista_monticulo.pop()
        if self.tamano_actual > 0:
            self.infilt_abajo(1)
        return valor_sacado