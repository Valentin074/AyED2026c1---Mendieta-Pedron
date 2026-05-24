# -*- coding: utf-8 -*-
from .Monticulo import MonticuloBinarioMinimo

class ColaPrioridad:
    def __init__(self):
        """
        Postcondición: Inicializa una cola de prioridad genérica vacía basada en un montículo mínimo.
        """
        self._contenedor = MonticuloBinarioMinimo()

    def esta_vacia(self):
        """
        Postcondición: Retorna True si la cola de prioridad no tiene elementos en espera.
        """
        return self._contenedor.esta_vacio()

    def desencolar(self):
        """
        Precondición: La cola de prioridad no debe estar vacía.
        Postcondición: Remueve y retorna el elemento con mayor prioridad (menor valor numérico).
        """
        if self.esta_vacia():
            raise IndexError("Error: Intento de desencolar en una cola de prioridad vacía.")
        return self._contenedor.eliminar_min()

    def encolar(self, elemento):
        """
        Precondición: El elemento debe ser comparable.
        Postcondición: Inserta el elemento en la cola de prioridad.
        """
        if elemento is None:
            raise ValueError("El elemento no puede ser nulo.")
        self._contenedor.insertar(elemento)

    def insertar(self, elemento):
        """
        Método alternativo para compatibilidad. Llama a encolar.
        """
        self.encolar(elemento)

    @property
    def tamano(self):
        """
        Postcondición: Retorna la cantidad actual de elementos en la cola.
        """
        return self._contenedor.tamano_actual

