from modelos.tablero import Tablero
from modelos.pieza import Rey

class Juego:
    
    def __init__(self):
        self._tablero = Tablero()
        self._turno_actual = "blanco"
        self._historial = []

    @property
    def turno_actual(self) -> str:
        return self._turno_actual

    @property
    def tablero(self) -> Tablero:
        return self._tablero

    def cambiar_turno(self):
        self._turno_actual = "negro" if self._turno_actual == "blanco" else "blanco"

    def ejecutar_movimiento(self, origen: tuple, destino: tuple) -> bool:
        pieza = self._tablero.obtener_pieza(origen[0], origen[1])
        if not pieza or pieza.color != self._turno_actual:
            return False

        movs_validos = pieza.movimientos_validos(self._tablero)
        if destino in movs_validos:
            dest_pieza = self._tablero.obtener_pieza(destino[0], destino[1])
            self._tablero.mover_pieza(origen, destino)
            
            notacion = f"{pieza.obtener_simbolo()} de {origen} a {destino}"
            self._historial.append(notacion)
            
            if isinstance(dest_pieza, Rey):
                return "victoria"

            self.cambiar_turno()
            return True
        return False

    def obtener_historial(self) -> list:
        return self._historial

    def reiniciar(self):
        self._tablero = Tablero()
        self._turno_actual = "blanco"
        self._historial.clear()