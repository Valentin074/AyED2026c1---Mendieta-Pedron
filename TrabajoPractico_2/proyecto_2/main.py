# -*- coding: utf-8 -*-
from modules.TemperaturasDB import Temperaturas_DB

def simular_base_de_datos():
    print("=" * 60)
    print(" BASE DE DATOS DE TEMPERATURAS EFICIENTE (TEMPERATURAS_DB)")
    print("=" * 60)

    db = Temperaturas_DB()

    datos_archivo = [
        ("15.2", "01/01/2026"),
        ("22.5", "10/01/2026"),
        ("34.1", "20/01/2026"),
        ("28.9", "05/02/2026"),
        ("12.0", "18/02/2026"),
        ("19.4", "01/03/2026")
    ]

    print("\n[+] Cargando muestras en la BD...")
    for temp, fecha in datos_archivo:
        db.guardar_temperatura(temp, fecha)
    print(f" -> Carga finalizada. Total registros en memoria: {db.cantidad_muestras()}")

    print("\n[?] Consultando temperatura del '20/01/2026':")
    print(f" -> Resultado: {db.devolver_temperatura('20/01/2026')} °C")

    f1, f2 = "05/01/2026", "20/02/2026"
    print(f"\n[?] Realizando consultas de rangos entre [{f1}] y [{f2}]:")
    print(f" -> Temperatura Máxima: {db.max_temp_rango(f1, f2)} °C")
    print(f" -> Temperatura Mínima: {db.min_temp_rango(f1, f2)} °C")
    
    extremos = db.temp_extremos_rango(f1, f2)
    print(f" -> Extremos en rango (Min, Max): {extremos}")

    print(f"\n[?] Listando mediciones en el rango [{f1} - {f2}]:")
    listado = db.devolver_temperaturas(f1, f2)
    for linea in listado:
        print(f"\t{linea}")

    fecha_borrar = "10/01/2026"
    print(f"\n[-] Eliminando el registro de la fecha: '{fecha_borrar}'")
    db.borrar_temperatura(fecha_borrar)
    print(f" -> Cantidad de muestras actual: {db.cantidad_muestras()}")

    print("\n" + "=" * 60)

if __name__ == "__main__":
    simular_base_de_datos()