# -*- coding: utf-8 -*-
import sys
import os
from datetime import datetime

directorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))
if directorio_raiz not in sys.path:
    sys.path.insert(0, directorio_raiz)

from biblioteca_ayed_fiuner.ayedfiuner.estructuras.ArbolAVL import ArbolAVL

class Temperaturas_DB:
    def __init__(self):
        self._arbol = ArbolAVL()

    def _convertir_fecha(self, fecha_str):
        try:
            return datetime.strptime(fecha_str.strip(), "%d/%m/%Y").date()
        except ValueError:
            raise ValueError(f"Formato de fecha inválido: '{fecha_str}'. Debe ser 'dd/mm/aaaa'.")

    def guardar_temperatura(self, temperatura, fecha):
        fecha_obj = self._convertir_fecha(fecha)
        self._arbol.insertar(fecha_obj, float(temperatura))

    def devolver_temperatura(self, fecha):
        fecha_obj = self._convertir_fecha(fecha)
        try:
            return self._arbol.buscar(fecha_obj)
        except KeyError:
            raise KeyError(f"No hay registros de temperatura para la fecha: {fecha}.")

    def _obtener_lista_rango(self, fecha1, fecha2):
        f1_obj = self._convertir_fecha(fecha1)
        f2_obj = self._convertir_fecha(fecha2)
        if f1_obj > f2_obj:
            raise ValueError("La fecha inicial debe ser menor o igual a la fecha final.")
        muestras = self._arbol.obtener_en_rango(f1_obj, f2_obj)
        if not muestras:
            raise ValueError(f"No se encontraron mediciones en el rango [{fecha1} - {fecha2}].")
        return muestras

    def max_temp_rango(self, fecha1, fecha2):
        muestras = self._obtener_lista_rango(fecha1, fecha2)
        return max(m[1] for m in muestras)

    def min_temp_rango(self, fecha1, fecha2):
        muestras = self._obtener_lista_rango(fecha1, fecha2)
        return min(m[1] for m in muestras)

    def temp_extremos_rango(self, fecha1, fecha2):
        muestras = self._obtener_lista_rango(fecha1, fecha2)
        temps = [m[1] for m in muestras]
        return min(temps), max(temps)

    def borrar_temperatura(self, fecha):
        fecha_obj = self._convertir_fecha(fecha)
        self._arbol.eliminar(fecha_obj)

    def devolver_temperaturas(self, fecha1, fecha2):
        f1_obj = self._convertir_fecha(fecha1)
        f2_obj = self._convertir_fecha(fecha2)
        muestras = self._arbol.obtener_en_rango(f1_obj, f2_obj)
        resultado = []
        for fecha_obj, temp in muestras:
            fecha_str = fecha_obj.strftime("%d/%m/%Y")
            resultado.append(f"{fecha_str}: {temp} ºC")
        return resultado

    def cantidad_muestras(self):
        return self._arbol.tamano

    def cargar_desde_archivo(self, ruta_archivo):
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"No se encontró el archivo de muestras en: {ruta_archivo}")
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                if linea_limpia and ";" in linea_limpia:
                    fecha, temp_str = linea_limpia.split(";")
                    self.guardar_temperatura(temp_str, fecha)