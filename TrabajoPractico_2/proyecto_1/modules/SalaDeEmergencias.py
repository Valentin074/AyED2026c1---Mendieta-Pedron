# -*- coding: utf-8 -*-
"""
Sala de emergencias - Integración con Cola de Prioridad Genérica
"""

import sys
import os
import time
import datetime
import random

directorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
if directorio_raiz not in sys.path:
    sys.path.insert(0, directorio_raiz)

from biblioteca_ayed_fiuner.ayedfiuner.estructuras.ColaPrioridad import ColaPrioridad
import Paciente as pac

n = 20  

cola_de_espera = ColaPrioridad()
contador_ingreso = 0  


for i in range(n):
    ahora = datetime.datetime.now()
    fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
    print('-*-'*15)
    print('\n', fecha_y_hora, '\n')

    paciente = pac.Paciente(contador_ingreso)
    contador_ingreso += 1
    
    prioridad_paciente = (paciente.get_riesgo(), contador_ingreso)
    cola_de_espera.encolar(paciente, prioridad=prioridad_paciente)
    print(f"Ingresa a sala de espera (Orden N° {contador_ingreso}): {paciente}")

    if random.random() < 0.5:
        if not cola_de_espera.esta_vacia():
            paciente_atendido = cola_de_espera.desencolar()
            print('*'*40)
            print('Se atiende el paciente:', paciente_atendido)
            print('*'*40)
        else:
            print('No hay pacientes en la cola de espera.')
    else:
        print('Los médicos se encuentran ocupados en el quirófano...')
    
    print()

    print('Pacientes que faltan atenderse:', cola_de_espera.tamano)
    for p in cola_de_espera.obtener_elementos():
        print('\t', p)
    
    print()
    print('-*-'*15)
    
    time.sleep(1)


