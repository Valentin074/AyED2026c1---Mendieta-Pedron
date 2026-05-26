# -*- coding: utf-8 -*-
import sys
import os

directorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
if directorio_raiz not in sys.path:
    sys.path.insert(0, directorio_raiz)

from biblioteca_ayed_fiuner.ayedfiuner.estructuras.Grafo import GrafoPesado

def cargar_red_desde_texto():
    """
    Postcondición: Instancia un grafo pesado y carga las aldeas y conexiones reales del archivo de texto.
    """
    g = GrafoPesado()
    
    aldeas = [
        "Lomaseca", "Pepino", "Los Infiernos", "El Cerrillo", "Peligros", 
        "Malcocinado", "Hortijos", "Humilladero", "Villaviciosa", "Cebolla", 
        "Torralta", "Silla", "La Pera", "Espera", "Elciego", "Diosleguarde", 
        "Melón", "Consuegra", "Aceituna", "La Aparecida", "Pancrudo", "Buenas Noches"
    ]
    
    for aldea in aldeas:
        g.agregar_vertice(aldea)
        
    conexiones = [
        ("Lomaseca", "Pepino", 3), ("Lomaseca", "Los Infiernos", 2), 
        ("Lomaseca", "El Cerrillo", 5), ("Lomaseca", "Peligros", 7),
        ("El Cerrillo", "Malcocinado", 6), ("Hortijos", "Humilladero", 5), 
        ("Hortijos", "Villaviciosa", 10), ("Hortijos", "Cebolla", 20),
        ("Torralta", "Silla", 4), ("Torralta", "Villaviciosa", 8), 
        ("Torralta", "Humilladero", 9), ("La Pera", "Los Infiernos", 3), 
        ("La Pera", "Pepino", 4), ("La Pera", "Espera", 3),
        ("Elciego", "Diosleguarde", 7), ("Elciego", "Melón", 3),
        ("Consuegra", "Malcocinado", 1), ("Malcocinado", "Aceituna", 2), 
        ("Malcocinado", "Peligros", 8), ("Malcocinado", "Diosleguarde", 9),
        ("Peligros", "La Aparecida", 5), ("Silla", "Pancrudo", 6), 
        ("Silla", "La Aparecida", 5), ("Cebolla", "Buenas Noches", 2), 
        ("Cebolla", "Pancrudo", 2), ("La Aparecida", "Pancrudo", 8), 
        ("La Aparecida", "Buenas Noches", 3), ("Melón", "Buenas Noches", 20)
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