# -*- coding: utf-8 -*-
"""
Sala de emergencias - Integración con Cola de Prioridad Genérica
"""

import sys
import os
import time
import datetime
import random

# Forzamos a Python a buscar en la raíz del proyecto para evitar el error de rutas
directorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
if directorio_raiz not in sys.path:
    sys.path.insert(0, directorio_raiz)

from biblioteca_ayed_fiuner.ayedfiuner.estructuras.ColaPrioridad import ColaPrioridad
import Paciente as pac

n = 20  # cantidad de ciclos de simulación

cola_de_espera = ColaPrioridad()
contador_ingreso = 0  # Criterio secundario para desempates

# Ciclo que gestiona la simulación
for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    # Creación de paciente
    paciente = pac.Paciente()
    contador_ingreso += 1
    
    # Encolamos usando 'encolar' (la tupla maneja la prioridad y el desempate por orden)
    cola_de_espera.encolar((paciente.get_riesgo(), contador_ingreso, paciente))
    print(f"Ingresa a sala de espera: {paciente}")

    # Atención de paciente en este ciclo (50% de probabilidad)
    if random.random() < 0.5:
        if not cola_de_espera.esta_vacia():
            tupla_atendida = cola_de_espera.desencolar()
            paciente_atendido = tupla_atendida[2] # Obtenemos el objeto Paciente
            print('*'*40)
            print('Se atiende el paciente:', paciente_atendido)
            print('*'*40)
        else:
            print('No hay pacientes en la cola de espera.')
    else:
        print('Los médicos se encuentran ocupados en el quirófano...')
    
    print()

    # Mostrar estado de la cola
    print('Pacientes que faltan atenderse:', cola_de_espera.tamano)
    for elemento in cola_de_espera._contenedor.lista_monticulo[1:]:
        print('\t', elemento[2])
    
    print()
    print('-*-'*15)
    
    time.sleep(1)