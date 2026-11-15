from modelos.pieza import Torre, Caballo, Alfil, Reina, Rey, Peon


class Tablero:

    def __init__(self):
        self._matriz = [[None for _ in range(8)] for _ in range(8)]
        self.inicializar_piezas()

    def inicializar_piezas(self):
        self._matriz[0] = [
            Torre("negro", 0, 0), Caballo("negro", 0, 1), Alfil("negro", 0, 2),
            Reina("negro", 0, 3), Rey("negro", 0, 4), Alfil("negro", 0, 5),
            Caballo("negro", 0, 6), Torre("negro", 0, 7)
        ]
        for c in range(8):
            self._matriz[1][c] = Peon("negro", 1, c)

        for c in range(8):
            self._matriz[6][c] = Peon("blanco", 6, c)
        self._matriz[7] = [
            Torre("blanco", 7, 0), Caballo(
                "blanco", 7, 1), Alfil("blanco", 7, 2),
            Reina("blanco", 7, 3), Rey("blanco", 7, 4), Alfil("blanco", 7, 5),
            Caballo("blanco", 7, 6), Torre("blanco", 7, 7)
        ]

    def obtener_pieza(self, fila: int, columna: int):
        return self._matriz[fila][columna]

    def mover_pieza(self, origen: tuple, destino: tuple) -> bool:
        origen_f, origen_c = origen
        dest_f, dest_c = destino
        pieza = self.obtener_pieza(origen_f, origen_c)

        if pieza:
            self._matriz[dest_f][dest_c] = pieza
            self._matriz[origen_f][origen_c] = None
            pieza.posicion = (dest_f, dest_c)
            return True
        return False
