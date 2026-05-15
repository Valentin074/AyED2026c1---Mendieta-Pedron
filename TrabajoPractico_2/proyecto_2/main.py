from datetime import datetime


class NodoAVL:
    def _init_(self, fecha, temperatura):
        self.fecha = fecha
        self.temperatura = temperatura

        self.izq = None
        self.der = None

        self.altura = 1


class AVL:
    def _init_(self):
        self.raiz = None
        self.tamano = 0

  
    # UTILIDADES
   
    def altura(self, nodo):
        if nodo is None:
            return 0
        return nodo.altura

    def balance(self, nodo):
        if nodo is None:
            return 0
        return self.altura(nodo.izq) - self.altura(nodo.der)

    def actualizar_altura(self, nodo):
        nodo.altura = 1 + max(self.altura(nodo.izq),
                              self.altura(nodo.der))

    # ROTACIONES

    def rotar_derecha(self, y):
        x = y.izq
        t2 = x.der

        x.der = y
        y.izq = t2

        self.actualizar_altura(y)
        self.actualizar_altura(x)

        return x

    def rotar_izquierda(self, x):
        y = x.der
        t2 = y.izq

        y.izq = x
        x.der = t2

        self.actualizar_altura(x)
        self.actualizar_altura(y)

        return y

    # INSERCIÓN

    def insertar(self, fecha, temperatura):
        self.raiz = self._insertar(self.raiz, fecha, temperatura)

    def _insertar(self, nodo, fecha, temperatura):

        if nodo is None:
            self.tamano += 1
            return NodoAVL(fecha, temperatura)

        if fecha < nodo.fecha:
            nodo.izq = self._insertar(nodo.izq, fecha, temperatura)

        elif fecha > nodo.fecha:
            nodo.der = self._insertar(nodo.der, fecha, temperatura)

        else:
            nodo.temperatura = temperatura
            return nodo

        self.actualizar_altura(nodo)

        balance = self.balance(nodo)

        # IZQ-IZQ
        if balance > 1 and fecha < nodo.izq.fecha:
            return self.rotar_derecha(nodo)

        # DER-DER
        if balance < -1 and fecha > nodo.der.fecha:
            return self.rotar_izquierda(nodo)

        # IZQ-DER
        if balance > 1 and fecha > nodo.izq.fecha:
            nodo.izq = self.rotar_izquierda(nodo.izq)
            return self.rotar_derecha(nodo)

        # DER-IZQ
        if balance < -1 and fecha < nodo.der.fecha:
            nodo.der = self.rotar_derecha(nodo.der)
            return self.rotar_izquierda(nodo)

        return nodo

    # BÚSQUEDA
   
    def buscar(self, fecha):
        return self._buscar(self.raiz, fecha)

    def _buscar(self, nodo, fecha):

        if nodo is None:
            return None

        if fecha == nodo.fecha:
            return nodo

        if fecha < nodo.fecha:
            return self._buscar(nodo.izq, fecha)

        return self._buscar(nodo.der, fecha)

    # ELIMINACIÓN
    
    def eliminar(self, fecha):
        self.raiz = self._eliminar(self.raiz, fecha)

    def _eliminar(self, nodo, fecha):

        if nodo is None:
            return nodo

        if fecha < nodo.fecha:
            nodo.izq = self._eliminar(nodo.izq, fecha)

        elif fecha > nodo.fecha:
            nodo.der = self._eliminar(nodo.der, fecha)

        else:

            self.tamano -= 1

            if nodo.izq is None:
                return nodo.der

            elif nodo.der is None:
                return nodo.izq

            temp = self.minimo(nodo.der)

            nodo.fecha = temp.fecha
            nodo.temperatura = temp.temperatura

            nodo.der = self._eliminar(nodo.der, temp.fecha)

        self.actualizar_altura(nodo)

        balance = self.balance(nodo)

        # IZQ-IZQ
        if balance > 1 and self.balance(nodo.izq) >= 0:
            return self.rotar_derecha(nodo)

        # IZQ-DER
        if balance > 1 and self.balance(nodo.izq) < 0:
            nodo.izq = self.rotar_izquierda(nodo.izq)
            return self.rotar_derecha(nodo)

        # DER-DER
        if balance < -1 and self.balance(nodo.der) <= 0:
            return self.rotar_izquierda(nodo)

        # DER-IZQ
        if balance < -1 and self.balance(nodo.der) > 0:
            nodo.der = self.rotar_derecha(nodo.der)
            return self.rotar_izquierda(nodo)

        return nodo

    def minimo(self, nodo):

        actual = nodo

        while actual.izq is not None:
            actual = actual.izq

        return actual

    # RECORRIDO EN RANGO
    
    def rango(self, fecha1, fecha2):

        resultado = []

        self._rango(self.raiz, fecha1, fecha2, resultado)

        return resultado

    def _rango(self, nodo, fecha1, fecha2, resultado):

        if nodo is None:
            return

        if fecha1 < nodo.fecha:
            self._rango(nodo.izq, fecha1, fecha2, resultado)

        if fecha1 <= nodo.fecha <= fecha2:
            resultado.append(nodo)

        if fecha2 > nodo.fecha:
            self._rango(nodo.der, fecha1, fecha2, resultado)


# BASE DE DATOS

class Temperaturas_DB:

    def _init_(self):
        self.avl = AVL()

    def convertir_fecha(self, fecha):
        return datetime.strptime(fecha, "%d/%m/%Y")


    def guardar_temperatura(self, temperatura, fecha):

        fecha_dt = self.convertir_fecha(fecha)

        self.avl.insertar(fecha_dt, temperatura)


    def devolver_temperatura(self, fecha):

        fecha_dt = self.convertir_fecha(fecha)

        nodo = self.avl.buscar(fecha_dt)

        if nodo:
            return nodo.temperatura

        return None


    def max_temp_rango(self, fecha1, fecha2):

        fecha1 = self.convertir_fecha(fecha1)
        fecha2 = self.convertir_fecha(fecha2)

        datos = self.avl.rango(fecha1, fecha2)

        return max(n.temperatura for n in datos)


    def min_temp_rango(self, fecha1, fecha2):

        fecha1 = self.convertir_fecha(fecha1)
        fecha2 = self.convertir_fecha(fecha2)

        datos = self.avl.rango(fecha1, fecha2)

        return min(n.temperatura for n in datos)


    def temp_extremos_rango(self, fecha1, fecha2):

        fecha1 = self.convertir_fecha(fecha1)
        fecha2 = self.convertir_fecha(fecha2)

        datos = self.avl.rango(fecha1, fecha2)

        temperaturas = [n.temperatura for n in datos]

        return min(temperaturas), max(temperaturas)


    def borrar_temperatura(self, fecha):

        fecha_dt = self.convertir_fecha(fecha)

        self.avl.eliminar(fecha_dt)


    def devolver_temperaturas(self, fecha1, fecha2):

        fecha1 = self.convertir_fecha(fecha1)
        fecha2 = self.convertir_fecha(fecha2)

        datos = self.avl.rango(fecha1, fecha2)

        lista = []

        for n in datos:
            fecha = n.fecha.strftime("%d/%m/%Y")
            lista.append(f"{fecha}: {n.temperatura} ºC")

        return lista

    def cantidad_muestras(self):
        return self.avl.tamano


    def cargar_archivo(self, nombre_archivo):

        with open(nombre_archivo, "r", encoding="utf-8") as archivo:

            for linea in archivo:

                fecha, temp = linea.strip().split(";")

                self.guardar_temperatura(float(temp), fecha)


# PRUEBAS

if _name_ == "_main_":

    db = Temperaturas_DB()

    db.cargar_archivo("muestras.txt")

    print("Cantidad de muestras:")
    print(db.cantidad_muestras())

    print("\nTemperatura del 10/02/2025:")
    print(db.devolver_temperatura("10/02/2025"))

    print("\nMáxima temperatura:")
    print(db.max_temp_rango("01/01/2025", "31/03/2025"))

    print("\nMínima temperatura:")
    print(db.min_temp_rango("01/01/2025", "31/03/2025"))

    print("\nExtremos:")
    print(db.temp_extremos_rango("01/01/2025", "31/03/2025"))

    print("\nTemperaturas en rango:")
    lista = db.devolver_temperaturas("01/02/2025", "05/02/2025")

    for x in lista:
        print(x)

    print("\nEliminando 10/02/2025")

    db.borrar_temperatura("10/02/2025")

    print(db.devolver_temperatura("10/02/2025"))