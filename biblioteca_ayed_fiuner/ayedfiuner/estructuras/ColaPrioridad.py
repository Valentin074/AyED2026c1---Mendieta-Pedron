class ColaPrioridad:
    def __init__(self):
        self.heap = []

    def esta_vacia(self):
        return len(self.heap) == 0
    
    def insertar(self, elemento):
        if elemento is None:
            raise ValueError("El elemento no puede ser nada")
        
        self.heap.append(elemento)
        self._subir(len(self.heap)-1)
        