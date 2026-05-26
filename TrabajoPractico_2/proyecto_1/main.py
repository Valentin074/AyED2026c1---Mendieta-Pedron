# -*- coding: utf-8 -*-

import time
import datetime
import random
import sys
import os

directorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
if directorio_raiz not in sys.path:
    sys.path.insert(0, directorio_raiz)

from biblioteca_ayed_fiuner.ayedfiuner.estructuras.ColaPrioridad import ColaPrioridad
import modules.paciente as pac

def ejecutar_simulacion():
    n = 20  
    cola_de_espera = ColaPrioridad()

    for i in range(n):
        ahora = datetime.datetime.now()
        fecha_y_hora = ahora.strftime('%d/%m/%Y %H:%M:%S')
        print('-*-'*15)
        print('\n', fecha_y_hora, '\n')

        paciente = pac.Paciente()
        
        cola_de_espera.encolar(paciente, prioridad=paciente.get_riesgo())
        print(f"Ingresa a sala de espera: {paciente}")

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

if __name__ == '__main__':
    ejecutar_simulacion()