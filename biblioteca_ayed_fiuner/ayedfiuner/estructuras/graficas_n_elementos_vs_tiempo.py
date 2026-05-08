import time
import matplotlib.pyplot as plt
from LDE import ListaDobleEnlazada  # Asegúrate que tu archivo se llame así

def realizar_analisis():
    # Tamaños de lista para probar (N)
    tamanos = [1000, 5000, 10000, 20000, 40000, 60000]
    
    tiempos_len = []
    tiempos_copiar = []
    tiempos_invertir = []

    for n in tamanos:
        # Preparación de la lista
        lista = ListaDobleEnlazada()
        for i in range(n):
            lista.agregar_al_final(i)

        # Medición de __len__ (O(1))
        # Se repite muchas veces para que el tiempo sea medible
        inicio = time.time()
        for _ in range(10000):
            _ = len(lista)
        tiempos_len.append((time.time() - inicio) / 10000)

        # Medición de copiar (O(n))
        inicio = time.time()
        _ = lista.copiar()
        tiempos_copiar.append(time.time() - inicio)

        # Medición de invertir (O(n))
        inicio = time.time()
        lista.invertir()
        tiempos_invertir.append(time.time() - inicio)

    # Configuración de la gráfica
    plt.figure(figsize=(10, 6))
    
    plt.plot(tamanos, tiempos_len, label='__len__ (O(1))', marker='o', linewidth=2)
    plt.plot(tamanos, tiempos_copiar, label='copiar (O(n))', marker='s', linewidth=2)
    plt.plot(tamanos, tiempos_invertir, label='invertir (O(n))', marker='^', linewidth=2)

    plt.title('N vs Tiempo de Ejecución (Eficiencia TAD)', fontsize=14)
    plt.xlabel('Cantidad de elementos (N)', fontsize=12)
    plt.ylabel('Tiempo de ejecución (segundos)', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Mostrar la gráfica
    plt.show()

if __name__ == "__main__":
    realizar_analisis()