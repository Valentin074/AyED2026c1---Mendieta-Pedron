# -*- coding: utf-8 -*-
import os
import sys

if 'modules.TemperaturasDB' in sys.modules:
    del sys.modules['modules.TemperaturasDB']

from modules.TemperaturasDB import Temperaturas_DB

def simular_base_de_datos_real():
    print("=" * 65)
    print(" BASE DE DATOS DE TEMPERATURAS - KEVIN KELVIN (PROBLEMA 2)")
    print("=" * 65)

    db = Temperaturas_DB()
    ruta_muestras = r"c:\Users\valen\OneDrive\Documentos\AyED2026c1---Mendieta-Pedron\TrabajoPractico_2\muestras.txt"
    
    print(f"\n[+] Leyendo archivo real desde: {ruta_muestras}")
    try:
        db.cargar_desde_archivo(ruta_muestras)
        print(f" -> Éxito. Total de muestras reales cargadas en el AVL: {db.cantidad_muestras()}")
    except Exception as e:
        print(f" -> Error al cargar el archivo: {e}")
        return

    fecha_consulta = "15/01/2025"
    print(f"\n[?] Operación devolver_temperatura('{fecha_consulta}'):")
    try:
        print(f" -> Resultado: {db.devolver_temperatura(fecha_consulta)} ºC")
    except KeyError as e:
        print(f" -> {e}")

    f1, f2 = "05/01/2025", "20/01/2025"
    print(f"\n[?] Consultas por rangos entre [{f1}] y [{f2}]:")
    print(f" -> max_temp_rango: {db.max_temp_rango(f1, f2)} ºC")
    print(f" -> min_temp_rango: {db.min_temp_rango(f1, f2)} ºC")
    print(f" -> temp_extremos_rango: {db.temp_extremos_rango(f1, f2)}")

    print(f"\n[?] devolver_temperaturas('{f1}', '{f2}') [Listado Ordenado]:")
    try:
        listado = db.devolver_temperaturas(f1, f2)
        for registro in listado:
            print(f"\t{registro}")
    except Exception as e:
        print(f" -> Error en rango: {e}")

    fecha_borrar = "10/01/2025"
    print(f"\n[-] Borrando la temperatura de la fecha: '{fecha_borrar}'")
    try:
        db.borrar_temperatura(fecha_borrar)
        print(f" -> Nueva cantidad de muestras totales en la BD: {db.cantidad_muestras()}")
    except Exception as e:
        print(f" -> Error al borrar: {e}")

    print("\n" + "=" * 65)

if __name__ == "__main__":
    simular_base_de_datos_real()