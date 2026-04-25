import time
import matplotlib.pyplot as plt
from ayedfiuner.estructuras.LDE import ListaDobleEnlazada

def medir_rendimiento():
    tamanos = [10, 100, 250, 500, 750, 1000, 1500, 2000]
    
    tiempos_len = []
    tiempos_copiar = []
    tiempos_invertir = []

    for n in tamanos:
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(i)
        
        inicio = time.perf_counter()
        _ = len(lista)
        fin = time.perf_counter()
        tiempos_len.append(fin - inicio)

        inicio = time.perf_counter()
        _ = lista.copiar()
        fin = time.perf_counter()
        tiempos_copiar.append(fin - inicio)

        inicio = time.perf_counter()
        lista.invertir()
        fin = time.perf_counter()
        tiempos_invertir.append(fin - inicio)

    plt.figure(figsize=(10, 6))
    plt.plot(tamanos, tiempos_len, label='len() - O(1)', marker='o')
    plt.plot(tamanos, tiempos_copiar, label='copiar() - O(n)', marker='s')
    plt.plot(tamanos, tiempos_invertir, label='invertir() - O(n)', marker='^')

    plt.title('Análisis de Complejidad: Lista Doble Enlazada')
    plt.xlabel('Cantidad de elementos (N)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.legend()
    plt.grid(True)
    
    plt.savefig('grafica_rendimiento_LDE.png')
    print("Gráfica generada con éxito como 'grafica_rendimiento_LDE.png'")
    plt.show()

if __name__ == "__main__":
    medir_rendimiento()