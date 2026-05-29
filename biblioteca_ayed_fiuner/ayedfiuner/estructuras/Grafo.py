# -*- coding: utf-8 -*-

class GrafoPesado:
    def __init__(self):
        """
        Postcondición: Inicializa un grafo pesado vacío utilizando un diccionario de adyacencia.
        """
        self.vertices = {}

    def agregar_vertice(self, vertice):
        """
        Precondición: El vértice no debe existir previamente en el grafo y no debe ser nulo.
        Postcondición: Añade el vértice al grafo con una lista de adyacencia vacía.
        """
        if vertice is None:
            raise ValueError("El nombre del vértice no puede ser nulo.")
        if vertice not in self.vertices:
            self.vertices[vertice] = {}

    def agregar_arista(self, u, v, peso):
        """
        Precondición: u y v deben ser vértices válidos ya existentes. El peso debe ser numérico y positivo.
        Postcondición: Añade una arista no dirigida entre u y v con el peso especificado.
        """
        if u not in self.vertices or v not in self.vertices:
            raise ValueError("Uno o ambos vértices no existen en el grafo.")
        if peso <= 0:
            raise ValueError("El peso debe ser un número mayor a cero.")
        
        self.vertices[u][v] = peso
        self.vertices[v][u] = peso

    def obtener_vecinos(self, vertice):
        """
        Precondición: El vértice debe existir en el grafo.
        Postcondición: Retorna un diccionario con los vecinos y los pesos de sus aristas.
        """
        if vertice not in self.vertices:
            raise ValueError("El vértice especificado no existe en el grafo.")
        return self.vertices[vertice]

    def obtener_vertices(self):
        """
        Precondición: Ninguna.
        Postcondición: Retorna una lista con todos los vértices del grafo.
        """
        return list(self.vertices.keys())