# -*- coding: utf-8 -*-
from modules.AgenciaNoticias import cargar_red_desde_texto, calcular_transmision_optima

def ejecutar_sistema_palomas():
    print("=" * 70)
    print("SISTEMA DE DISTRIBUCIÓN DE NOTICIAS EFICIENTE - PALOMAS WILLIAM")
    print("=" * 70)
    
    grafo_red = cargar_red_desde_texto()
    origen_principal = "Peligros"
    
    arbol_expansion, kms_totales = calcular_transmision_optima(grafo_red, inicio=origen_principal)
    
    aldeas_sistema = grafo_red.obtener_vertices()
    aldeas_sistema.sort()
    
    envios_desde_nodo = {}
    for nodo in aldeas_sistema:
        envios_desde_nodo[nodo] = []
        
    for destino, (origen, peso) in arbol_expansion.items():
        envios_desde_nodo[origen].append(destino)
        
    print(f"\nEmisor inicial del mensaje: {origen_principal}\n")
    print(f"{'ALDEA':<18} | {'RECIBE DE':<18} | {'REPLICA A (ENVIARA)'}")
    print("-" * 70)
    
    for aldea in aldeas_sistema:
        replicas = ", ".join(envios_desde_nodo[aldea])
        if not replicas:
            replicas = "Ninguna (Fin de rama)"
            
        if aldea == origen_principal:
            print(f"{aldea:<18} | {'EMISOR ORIGEN':<18} | {replicas}")
        else:
            padre, _ = arbol_expansion[aldea]
            print(f"{aldea:<18} | {padre:<18} | {replicas}")
            
    print("-" * 70)
    print(f"Suma total de distancias recorridas por todas las palomas: {kms_totales} leguas.")
    print("=" * 70)

if __name__ == "__main__":
    ejecutar_sistema_palomas()