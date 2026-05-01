def ordenamiento_quicksort(lista):
    """
    Ordena una lista usando Quicksort.
    Pre: lista debe contener elementos comparables.
    Post: Retorna una nueva lista ordenada.
    """
    if not isinstance(lista, list):
        raise TypeError("Se esperaba una lista")
    if len(lista) <= 1:
        return lista
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    return ordenamiento_quicksort(menores) + iguales + ordenamiento_quicksort(mayores)