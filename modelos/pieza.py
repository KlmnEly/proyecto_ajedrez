from abc import ABC, abstractmethod


class Pieza(ABC):

    def __init__(self, color: str, fila: int, columna: int):
        self._color = color  
        self._fila = fila
        self._columna = columna
        self._movida = False

    @property
    def color(self) -> str:
        return self._color

    @property
    def posicion(self) -> tuple:
        return (self._fila, self._columna)

    @posicion.setter
    def posicion(self, nueva_pos: tuple):
        self._fila, self._columna = nueva_pos
        self._movida = True

    @abstractmethod
    def obtener_simbolo(self) -> str:
        """Retorna el carácter Unicode de la pieza."""
        pass

    @abstractmethod
    def movimientos_validos(self, tablero) -> list:
        """Calcula los movimientos válidos según las reglas de la pieza (Polimorfismo)."""
        pass


class Torre(Pieza):
    def obtener_simbolo(self) -> str:
        return "♖" if self._color == "blanco" else "♜"

    def movimientos_validos(self, tablero) -> list:
        movs = []
        direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for df, dc in direcciones:
            f, c = self._fila + df, self._columna + dc
            while 0 <= f < 8 and 0 <= c < 8:
                destino = tablero.obtener_pieza(f, c)
                if destino is None:
                    movs.append((f, c))
                else:
                    if destino.color != self._color:
                        movs.append((f, c))
                    break
                f += df
                c += dc
        return movs


class Alfil(Pieza):
    def obtener_simbolo(self) -> str:
        return "♗" if self._color == "blanco" else "♝"

    def movimientos_validos(self, tablero) -> list:
        movs = []
        direcciones = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for df, dc in direcciones:
            f, c = self._fila + df, self._columna + dc
            while 0 <= f < 8 and 0 <= c < 8:
                destino = tablero.obtener_pieza(f, c)
                if destino is None:
                    movs.append((f, c))
                else:
                    if destino.color != self._color:
                        movs.append((f, c))
                    break
                f += df
                c += dc
        return movs


class Reina(Pieza):
    def obtener_simbolo(self) -> str:
        return "♕" if self._color == "blanco" else "♛"

    def movimientos_validos(self, tablero) -> list:
        torre_simulada = Torre(self._color, self._fila, self._columna)
        alfil_simulado = Alfil(self._color, self._fila, self._columna)
        return torre_simulada.movimientos_validos(tablero) + alfil_simulado.movimientos_validos(tablero)


class Rey(Pieza):
    def obtener_simbolo(self) -> str:
        return "♔" if self._color == "blanco" else "♚"

    def movimientos_validos(self, tablero) -> list:
        movs = []
        direcciones = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                       (0, 1), (1, -1), (1, 0), (1, 1)]
        for df, dc in direcciones:
            f, c = self._fila + df, self._columna + dc
            if 0 <= f < 8 and 0 <= c < 8:
                destino = tablero.obtener_pieza(f, c)
                if destino is None or destino.color != self._color:
                    movs.append((f, c))
        return movs


class Caballo(Pieza):
    def obtener_simbolo(self) -> str:
        return "♘" if self._color == "blanco" else "♞"

    def movimientos_validos(self, tablero) -> list:
        movs = []
        saltos = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                  (1, -2), (1, 2), (2, -1), (2, 1)]
        for df, dc in saltos:
            f, c = self._fila + df, self._columna + dc
            if 0 <= f < 8 and 0 <= c < 8:
                destino = tablero.obtener_pieza(f, c)
                if destino is None or destino.color != self._color:
                    movs.append((f, c))
        return movs


class Peon(Pieza):
    def obtener_simbolo(self) -> str:
        return "♙" if self._color == "blanco" else "♟"

    def movimientos_validos(self, tablero) -> list:
        movs = []
        dir_f = -1 if self._color == "blanco" else 1
        f, c = self._fila + dir_f, self._columna

        if 0 <= f < 8 and tablero.obtener_pieza(f, c) is None:
            movs.append((f, c))
            f_doble = self._fila + (dir_f * 2)
            if not self._movida and tablero.obtener_pieza(f_doble, c) is None and tablero.obtener_pieza(f, c) is None:
                movs.append((f_doble, c))

        for dc in [-1, 1]:
            nf, nc = self._fila + dir_f, self._columna + dc
            if 0 <= nf < 8 and 0 <= nc < 8:
                destino = tablero.obtener_pieza(nf, nc)
                if destino is not None and destino.color != self._color:
                    movs.append((nf, nc))
        return movs
