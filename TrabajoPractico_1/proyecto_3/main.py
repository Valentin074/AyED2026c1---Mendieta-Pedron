import time
import random
import matplotlib.pyplot as plt
from ayedfiuner.algoritmos.burbuja import ordenamiento_burbuja
from ayedfiuner.algoritmos.quicksort import ordenamiento_quicksort
from ayedfiuner.algoritmos.radix import ordenamiento_radix

def medir_tiempos():
    tallas = range(1, 1001, 50)
    tiempos_bubble = []
    tiempos_quick = []
    tiempos_radix = []
    tiempos_sorted = []

    for n in tallas:
        lista_original = [random.randint(10000, 99999) for _ in range(n)]

        copia = lista_original[:]
        inicio = time.time()
        ordenamiento_burbuja(copia)
        tiempos_bubble.append(time.time() - inicio)

        copia = lista_original[:]
        inicio = time.time()
        ordenamiento_quicksort(copia)
        tiempos_quick.append(time.time() - inicio)

        copia = lista_original[:]
        inicio = time.time()
        ordenamiento_radix(copia)
        tiempos_radix.append(time.time() - inicio)

        copia = lista_original[:]
        inicio = time.time()
        sorted(copia)
        tiempos_sorted.append(time.time() - inicio)

    plt.figure(figsize=(10, 6))
    plt.plot(tallas, tiempos_bubble, label='Burbuja')
    plt.plot(tallas, tiempos_quick, label='Quicksort')
    plt.plot(tallas, tiempos_radix, label='Radix Sort')
    plt.plot(tallas, tiempos_sorted, label='Python Sorted')
    plt.xlabel('N (Elementos)')
    plt.ylabel('Tiempo (segundos)')
    plt.title('Comparativa de Algoritmos - Problema 3')
    plt.legend()
    plt.grid(True)
    plt.show()

if _name_ == "_main_":
    medir_tiempos()