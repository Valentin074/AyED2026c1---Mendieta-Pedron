def ordenamiento_burbuja(lis):
    """
    Ordena una lista de elementos comparables utilizando el algoritmo de burbuja.
    Pre: lis debe ser una lista con elementos comparables.
    Post: La lista original es modificada y queda ordenada de menor a mayor.
    """
    n = len(lis)
    for i in range(n):
        hubo_intercambio = False
        for j in range(0, n-i-1):
            if lis[j] > lis[j+1]:
                aux = lis[j]
                lis[j] = lis[j+1]
                lis[j+1] = aux
                hubo_intercambio = True
        if not hubo_intercambio:
            break
    return lis


if __name__ == "__main__":
    # Prueba local del algoritmo de ordenamiento burbuja
    ejemplo_lis = [64, 34, 25, 12, 22, 11, 90]
    lis_ordenada = ordenamiento_burbuja(ejemplo_lis)
    print("Lista ordenada:", lis_ordenada)