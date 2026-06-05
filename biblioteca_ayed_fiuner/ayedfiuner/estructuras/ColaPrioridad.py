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
        
        prioridad, elemento = self._contenedor.eliminar_min()
        return elemento

    def encolar(self, elemento, prioridad):
        """
        Precondición: El elemento no debe ser nulo y la prioridad debe ser comparable.
        Postcondición: Inserta el elemento en la cola utilizando la prioridad indicada. 
        """
        if elemento is None:
            raise ValueError("El elemento no puede ser nulo.")
        if prioridad is None:
            raise ValueError("La prioridad no puede ser nula.")
        
        self._contenedor.insertar((prioridad, elemento))

    def insertar(self, elemento, prioridad):
        """
        Método alternativo para compatibilidad. Llama a encolar.
        """
        self.encolar(elemento, prioridad)

    @property
    def tamano(self):
        """
        Postcondición: Retorna la cantidad actual de elementos en la cola.
        """
        return self._contenedor.tamano_actual

    def obtener_elementos(self):
        """
        Postcondición: Devuelve una lista con los elementos actualmente encolados 
                       (manteniendo el formato interno) para visualización lícita.
        """
        return [item[1] for item in self._contenedor.lista_monticulo[1:]]


