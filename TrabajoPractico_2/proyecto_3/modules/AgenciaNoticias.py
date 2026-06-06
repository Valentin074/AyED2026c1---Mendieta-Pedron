# -*- coding: utf-8 -*-
import sys
import os

directorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
if directorio_raiz not in sys.path:
    sys.path.insert(0, directorio_raiz)

from biblioteca_ayed_fiuner.ayedfiuner.estructuras.Grafo import GrafoPesado

def cargar_red_desde_texto():
    """
    Postcondición: Instancia un grafo pesado y carga las aldeas y conexiones 
                   reales leyendo dinámicamente desde el archivo 'aldeas.txt'.
    """
    g = GrafoPesado()
    
    ruta_archivo = os.path.join(os.path.dirname(__file__), '../data/aldeas.txt')
    
    if not os.path.exists(ruta_archivo):
        raise FileNotFoundError(f"No se encontró el archivo de datos en: {ruta_archivo}")

    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for nro_linea, linea in enumerate(archivo, 1):
            linea_limpia = linea.strip()
            
            if not linea_limpia or linea_limpia == '"aldeas.txt"':
                continue
                
            partes = [p.strip() for p in linea_limpia.split(',')]
            
            if len(partes) == 3:
                u, v, peso_str = partes
                try:
                    peso = int(peso_str)
                    
                    g.agregar_vertice(u)
                    g.agregar_vertice(v)
                    g.agregar_arista(u, v, peso)
                except ValueError:
                    print(f"Advertencia: Línea {nro_linea} ignorada por peso inválido: '{linea_limpia}'")
            
            elif len(partes) == 1:
                aldea_aislada = partes[0]
                if aldea_aislada:
                    g.agregar_vertice(aldea_aislada)
                    
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