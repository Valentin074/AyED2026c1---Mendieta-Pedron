# mazo.py

from biblioteca_ayed_fiuner.ayedfiuner.estructuras.LDE import ListaDobleEnlazada

class DequeEmptyError(Exception):
    """Se lanza cuando el mazo no tiene más cartas."""
    pass

class Mazo:
    def __init__(self):
        
        self.__cartas = ListaDobleEnlazada()

    def poner_carta_arriba(self, carta):
        """Equivale a agregar al inicio de la lista."""
        self.__cartas.agregar_al_inicio(carta)

    def poner_carta_abajo(self, carta):
        """Equivale a agregar al final de la lista."""
        self.__cartas.agregar_al_final(carta)

    def sacar_carta_arriba(self, mostrar=False):
        """
        Quita la primera carta. Lanza DequeEmptyError si está vacío.
        Si el juego pide 'mostrar', ponemos la carta bocal arriba.
        """
        if self.__cartas.esta_vacia():
            raise DequeEmptyError("No quedan cartas en el mazo")
        
        
        carta = self.__cartas.extraer(0)
        
        if mostrar:
            carta.visible = True
        return carta

    def __len__(self):
        """Permite que len(mazo) funcione en la lógica del juego."""
        return len(self.__cartas)

    def __str__(self):
        """Muestra el contenido del mazo usando el str de la lista."""
        return str(self.__cartas)
    