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
        """
        Postcondición: Crea una base de datos de temperaturas basada en un Árbol AVL interno.
        """
        self._arbol = ArbolAVL()

    def _convertir_fecha(self, fecha_str):
        """
        Precondición: El parámetro 'fecha_str' debe ser un string con formato 'dd/mm/aaaa'.
        Postcondición: Retorna un objeto de tipo datetime.date correspondiente.
        Excepciones: Lanza ValueError si el formato es inválido.
        """
        try:
            return datetime.strptime(fecha_str.strip(), "%d/%m/%Y").date()
        except ValueError:
            raise ValueError(f"Formato de fecha inválido: '{fecha_str}'. Debe ser 'dd/mm/aaaa'.")

    def guardar_temperatura(self, temperatura, fecha):
        """
        Precondición: 'fecha' debe cumplir el formato 'dd/mm/aaaa' y 'temperatura' debe ser convertible a número.
        Postcondición: Almacena o actualiza la temperatura en la base de datos asociada a la fecha dada.
        Excepciones: Lanza ValueError si los parámetros son inválidos.
        """
        fecha_obj = self._convertir_fecha(fecha)
        self._arbol.insertar(fecha_obj, float(temperatura))

    def devolver_temperatura(self, fecha):
        """
        Precondición: 'fecha' debe ser un string en formato 'dd/mm/aaaa' y debe estar registrada en el sistema.
        Postcondición: Retorna el valor flotante de la temperatura asociada a la fecha dada.
        Excepciones: Lanza KeyError si la fecha no tiene registros y ValueError por formato inválido.
        """
        fecha_obj = self._convertir_fecha(fecha)
        try:
            return self._arbol.buscar(fecha_obj)
        except KeyError:
            raise KeyError(f"No hay registros de temperatura para la fecha: {fecha}.")

    def _obtener_lista_rango(self, fecha1, fecha2):
        """
        Precondición: Las fechas deben tener el formato 'dd/mm/aaaa' y cumplir que fecha1 <= fecha2.
        Postcondición: Retorna una lista de mediciones dentro de las fechas limites.
        Excepciones: Lanza ValueError si fecha1 > fecha2 o si no se hallan registros.
        """
        f1_obj = self._convertir_fecha(fecha1)
        f2_obj = self._convertir_fecha(fecha2)
        if f1_obj > f2_obj:
            raise ValueError("La fecha inicial debe ser menor o igual a la fecha final.")
        muestras = self._arbol.obtener_en_rango(f1_obj, f2_obj)
        if not muestras:
            raise ValueError(f"No se encontraron mediciones en el rango [{fecha1} - {fecha2}].")
        return muestras

    def max_temp_rango(self, fecha1, fecha2):
        """
        Precondición: Rango de fechas válido 'dd/mm/aaaa' con fecha1 <= fecha2 y con mediciones existentes.
        Postcondición: Retorna la temperatura máxima encontrada en el rango indicado.
        Excepciones: Lanza ValueError si los parámetros o el rango son incorrectos.
        """
        muestras = self._obtener_lista_rango(fecha1, fecha2)
        return max(m[1] for m in muestras)

    def min_temp_rango(self, fecha1, fecha2):
        """
        Precondición: Rango de fechas válido 'dd/mm/aaaa' con fecha1 <= fecha2 y con mediciones existentes.
        Postcondición: Retorna la temperatura mínima encontrada en el rango indicado.
        Excepciones: Lanza ValueError si los parámetros o el rango son incorrectos.
        """
        muestras = self._obtener_lista_rango(fecha1, fecha2)
        return min(m[1] for m in muestras)

    def temp_extremos_rango(self, fecha1, fecha2):
        """
        Precondición: Rango de fechas válido 'dd/mm/aaaa' con fecha1 <= fecha2 y con mediciones existentes.
        Postcondición: Retorna una tupla (mínimo, máximo) con los extremos térmicos del rango.
        Excepciones: Lanza ValueError si los parámetros o el rango son incorrectos.
        """
        muestras = self._obtener_lista_rango(fecha1, fecha2)
        temps = [m[1] for m in muestras]
        return min(temps), max(temps)

    def borrar_temperatura(self, fecha):
        """
        Precondición: 'fecha' en formato string 'dd/mm/aaaa' existente en la base de datos.
        Postcondición: Elimina el registro térmico y rebalancea la estructura.
        Excepciones: Lanza KeyError si la fecha no existe y ValueError si el formato es inválido.
        """
        fecha_obj = self._convertir_fecha(fecha)
        self._arbol.eliminar(fecha_obj)

    def devolver_temperaturas(self, fecha1, fecha2):
        """
        Precondición: Las fechas deben tener el formato 'dd/mm/aaaa' y cumplir que fecha1 <= fecha2.
        Postcondición: Devuelve una lista ordenada cronológicamente de strings formateados con "dd/mm/aaaa: temperatura ºC".
        Excepciones: Lanza ValueError por inconsistencia de fechas o formato.
        """
        f1_obj = self._convertir_fecha(fecha1)
        f2_obj = self._convertir_fecha(fecha2)
        if f1_obj > f2_obj:
            raise ValueError("La fecha inicial debe ser menor o igual a la fecha final.")
        muestras = self._arbol.obtener_en_rango(f1_obj, f2_obj)
        resultado = []
        for fecha_obj, temp in muestras:
            fecha_str = fecha_obj.strftime("%d/%m/%Y")
            resultado.append(f"{fecha_str}: {temp} ºC")
        return resultado

    def cantidad_muestras(self):
        """
        Postcondición: Retorna un número entero con la cantidad de muestras totales cargadas en el sistema.
        """
        return self._arbol.tamano

    def cargar_desde_archivo(self, ruta_archivo):
        """
        Precondición: La ruta dada debe existir en el sistema de almacenamiento de archivos.
        Postcondición: Lee las muestras línea a línea e inserta los datos en el árbol AVL.
        Excepciones: Lanza FileNotFoundError si el archivo no existe.
        """
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"No se encontró el archivo de muestras en: {ruta_archivo}")
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                linea_limpia = linea.strip()
                if linea_limpia and ";" in linea_limpia:
                    fecha, temp_str = linea_limpia.split(";")
                    self.guardar_temperatura(temp_str, fecha)