def ordenamiento_radix(lista):
    """
    Ordena una lista de enteros usando Radix Sort.
    Pre: lista de números enteros.
    Post: Retorna una nueva lista ordenada.
    """
    if not isinstance(lista, list):
        raise TypeError("Se esperaba una lista")
    if not lista: return []
    arr = lista.copy()
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        n = len(arr)
        salida = [0] * n
        conteo = [0] * 10
        for i in arr:
            conteo[(i // exp) % 10] += 1
        for i in range(1, 10):
            conteo[i] += conteo[i - 1]
        for i in range(len(arr) - 1, -1, -1):
            indice = (arr[i] // exp) % 10
            salida[conteo[indice] - 1] = arr[i]
            conteo[indice] -= 1
        arr = salida[:]
        exp *= 10
    return arr