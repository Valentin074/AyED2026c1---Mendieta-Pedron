# -*- coding: utf-8 -*-
import sys
import os

directorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
if directorio_raiz not in sys.path:
    sys.path.insert(0, directorio_raiz)

from biblioteca_ayed_fiuner.ayedfiuner.estructuras.Grafo import GrafoPesado

def cargar_red_desde_texto():
    """
    Postcondición: Instancia un grafo pesado y carga las 21 aldeas vecinas leyendo el formato de tuplas.
    """
    g = GrafoPesado()
    
    aldeas = [
        "Peligros", "Alfacar", "Vizmar", "Calicasas", "Cogollos", "Guevejar", 
        "Nivar", "Pulianas", "Maracena", "Jun", "Granada", "Armilla", 
        "Churriana", "Gabia", "Cullar", "Ogijares", "Gojar", "Dilar", 
        "Otura", "Alhendin", "Padul"
    ]
    
    for aldea in aldeas:
        g.agregar_vertice(aldea)
        
    conexiones = [
        ("Peligros", "Alfacar", 5), ("Peligros", "Pulianas", 3), ("Peligros", "Calicasas", 7),
        ("Alfacar", "Vizmar", 4), ("Alfacar", "Jun", 6), ("Vizmar", "Cogollos", 8),
        ("Calicasas", "Cogollos", 6), ("Pulianas", "Guevejar", 4), ("Pulianas", "Maracena", 3),
        ("Guevejar", "Nivar", 3), ("Maracena", "Jun", 2), ("Maracena", "Granada", 4),
        ("Maracena", "Armilla", 5), ("Granada", "Jun", 3), ("Granada", "Armilla", 5),
        ("Granada", "Cullar", 6), ("Armilla", "Churriana", 4), ("Armilla", "Ogijares", 3),
        ("Churriana", "Gabia", 3), ("Gabia", "Alhendin", 5), ("Cullar", "Ogijares", 2),
        ("Ogijares", "Gojar", 4), ("Ogijares", "Otura", 7), ("Gojar", "Dilar", 5),
        ("Dilar", "Otura", 3), ("Otura", "Alhendin", 4), ("Alhendin", "Padul", 6)
    ]
    
    for u, v, peso in conexiones:
        g.agregar_arista(u, v, peso)
        
    return g

def calcular_transmision_optima(grafo, inicio="Peligros"):
    """
    Precondición: El grafo debe contener al nodo de inicio.
    Postcondición: Retorna un diccionario con la estructura de distribución óptima (MST) y la distancia total.
    """
    if inicio not in grafo.obtener_vertices():
        raise ValueError("La aldea especificada como emisor inicial no existe en el grafo.")

    visitados = set([inicio])
    transmision = {}  
    distancia_total = 0
    num_vertices = len(grafo.obtener_vertices())

    while len(visitados) < num_vertices:
        arista_optima = None
        for u in visitados:
            for v, peso in grafo.obtener_vecinos(u).items():
                if v not in visitados:
                    if arista_optima is None or peso < arista_optima[2]:
                        arista_optima = (u, v, peso)
        
        if arista_optima is None:
            break
            
        origen, destino, peso = arista_optima
        visitados.add(destino)
        transmision[destino] = (origen, peso)
        distancia_total += peso

    return transmision, distancia_total