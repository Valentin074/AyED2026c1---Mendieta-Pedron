# -*- coding: utf-8 -*-

class NodoAVL:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izquierdo = None
        self.derecho = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        """
        Postcondición: Crea un árbol AVL vacío con raíz nula y tamaño en 0.
        """
        self.raiz = None
        self._tamano = 0

    @property
    def tamano(self):
        """
        Postcondición: Retorna la cantidad de elementos en el árbol.
        """
        return self._tamano

    def obtener_altura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura

    def obtener_balance(self, nodo):
        if not nodo:
            return 0
        return self.obtener_altura(nodo.izquierdo) - self.obtener_altura(nodo.derecho)

    def rotar_derecha(self, y):
        x = y.izquierdo
        T2 = x.derecho
        x.derecho = y
        y.izquierdo = T2
        y.altura = 1 + max(self.obtener_altura(y.izquierdo), self.obtener_altura(y.derecho))
        x.altura = 1 + max(self.obtener_altura(x.izquierdo), self.obtener_altura(x.derecho))
        return x

    def rotar_izquierda(self, x):
        y = x.derecho
        T2 = y.izquierdo
        y.izquierdo = x
        x.derecho = T2
        x.altura = 1 + max(self.obtener_altura(x.izquierdo), self.obtener_altura(x.derecho))
        y.altura = 1 + max(self.obtener_altura(y.izquierdo), self.obtener_altura(y.derecho))
        return y

    def insertar(self, clave, valor):
        """
        Precondición: La clave debe ser comparable y no nula.
        Postcondición: Inserta o actualiza la clave con su valor manteniendo el balance AVL.
        Excepciones: Lanza ValueError si la clave es None.
        """
        if clave is None:
            raise ValueError("La clave no puede ser nula.")
        self.raiz = self._insertar_recursivo(self.raiz, clave, valor)

    def _insertar_recursivo(self, nodo, clave, valor):
        if not nodo:
            self._tamano += 1
            return NodoAVL(clave, valor)

        if clave < nodo.clave:
            nodo.izquierdo = self._insertar_recursivo(nodo.izquierdo, clave, valor)
        elif clave > nodo.clave:
            nodo.derecho = self._insertar_recursivo(nodo.derecho, clave, valor)
        else:
            nodo.valor = valor
            return nodo

        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierdo), self.obtener_altura(nodo.derecho))
        balance = self.obtener_balance(nodo)

       
        if balance > 1 and clave < nodo.izquierdo.clave:
            return self.rotar_derecha(nodo)
       
        if balance < -1 and clave > nodo.derecho.clave:
            return self.rotar_izquierda(nodo)
     
        if balance > 1 and clave > nodo.izquierdo.clave:
            nodo.izquierdo = self.rotar_izquierda(nodo.izquierdo)
            return self.rotar_derecha(nodo)
        
        if balance < -1 and clave < nodo.derecho.clave:
            nodo.derecho = self.rotar_derecha(nodo.derecho)
            return self.rotar_izquierda(nodo)

        return nodo

    def buscar(self, clave):
        """
        Precondición: La clave debe existir en el árbol y no ser nula.
        Postcondición: Retorna el valor asociado a la clave.
        Excepciones: Lanza ValueError si la clave es None y KeyError si no se encuentra.
        """
        if clave is None:
            raise ValueError("La clave no puede ser nula.")
        nodo = self._buscar_recursivo(self.raiz, clave)
        if not nodo:
            raise KeyError(f"La clave '{clave}' no se encuentra registrada.")
        return nodo.valor

    def _buscar_recursivo(self, nodo, clave):
        if not nodo or nodo.clave == clave:
            return nodo
        if clave < nodo.clave:
            return self._buscar_recursivo(nodo.izquierdo, clave)
        return self._buscar_recursivo(nodo.derecho, clave)

    def eliminar(self, clave):
        """
        Precondición: La clave debe existir en el árbol y no ser nula.
        Postcondición: Remueve la clave del árbol rebalanceándolo.
        Excepciones: Lanza ValueError si la clave es None y KeyError si la clave no existe.
        """
        if clave is None:
            raise ValueError("La clave no puede ser nula.")
        self.raiz = self._eliminar_recursivo(self.raiz, clave)

    def _eliminar_recursivo(self, nodo, clave, restar_tamano=True):
        if not nodo:
            raise KeyError(f"La clave '{clave}' no existe para ser eliminada.")

        if clave < nodo.clave:
            nodo.izquierdo = self._eliminar_recursivo(nodo.izquierdo, clave, restar_tamano)
        elif clave > nodo.clave:
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, clave, restar_tamano)
        else:
            if restar_tamano:
                self._tamano -= 1
            if not nodo.izquierdo:
                return nodo.derecho
            elif not nodo.derecho:
                return nodo.izquierdo

            temp = self._obtener_nodo_minimo(nodo.derecho)
            nodo.clave = temp.clave
            nodo.valor = temp.valor
            nodo.derecho = self._eliminar_recursivo(nodo.derecho, temp.clave, restar_tamano=False)

        nodo.altura = 1 + max(self.obtener_altura(nodo.izquierdo), self.obtener_altura(nodo.derecho))
        balance = self.obtener_balance(nodo)

        if balance > 1 and self.obtener_balance(nodo.izquierdo) >= 0:
            return self.rotar_derecha(nodo)
        if balance > 1 and self.obtener_balance(nodo.izquierdo) < 0:
            nodo.izquierdo = self.rotar_izquierda(nodo.izquierdo)
            return self.rotar_derecha(nodo)
        if balance < -1 and self.obtener_balance(nodo.derecho) <= 0:
            return self.rotar_izquierda(nodo)
        if balance < -1 and self.obtener_balance(nodo.derecho) > 0:
            nodo.derecho = self.rotar_derecha(nodo.derecho)
            return self.rotar_izquierda(nodo)

        return nodo

    def _obtener_nodo_minimo(self, nodo):
        actual = nodo
        while actual.izquierdo:
            actual = actual.izquierdo
        return actual

    def obtener_en_rango(self, inicio, fin):
        """
        Postcondición: Devuelve una lista ordenada de tuplas (clave, valor) contenidas en el rango inclusive.
        """
        resultado = []
        self._rango_recursivo(self.raiz, inicio, fin, resultado)
        return resultado

    def _rango_recursivo(self, nodo, inicio, fin, resultado):
        if not nodo:
            return
        if inicio < nodo.clave:
            self._rango_recursivo(nodo.izquierdo, inicio, fin, resultado)
        if inicio <= nodo.clave <= fin:
            resultado.append((nodo.clave, nodo.valor))
        if fin > nodo.clave:
            self._rango_recursivo(nodo.derecho, inicio, fin, resultado)