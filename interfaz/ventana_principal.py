import tkinter as tk
from tkinter import messagebox
from modelos.juego import Juego


class VentanaPrincipal:

    def __init__(self, root):
        self.root = root
        self.root.title("Ajedrez")
        self.root.geometry("850x650")
        self.root.minsize(800, 600)

        self.juego = Juego()
        self.origen_seleccionado = None

        self.crear_widgets()
        self.actualizar_tablero_visual()

    def crear_widgets(self):
        lbl_titulo = tk.Label(
            self.root, 
            text="♟ Ajedrez Académico POO ♟", 
            font=("Arial", 16, "bold"), 
            fg="#2c3e50"
        )
        lbl_titulo.pack(pady=10)

        contenedor = tk.Frame(self.root)
        contenedor.pack(fill=tk.BOTH, expand=True, padx=15, pady=5)

        self.frame_tablero = tk.Frame(
            contenedor, bg="#34495e", bd=3, relief=tk.RAISED
        )
        self.frame_tablero.pack(side=tk.LEFT, padx=10)

        self.botones_casillas = [[None for _ in range(8)] for _ in range(8)]
        for f in range(8):
            for c in range(8):
                color_fondo = "#f0d9b5" if (f + c) % 2 == 0 else "#b58863"
                btn = tk.Button(
                    self.frame_tablero, text="", font=("Arial", 28), width=2, height=1,
                    bg=color_fondo, activebackground="#769656",
                    command=lambda fila=f, col=c: self.clic_casilla(fila, col)
                )
                btn.grid(row=f, column=c, padx=1, pady=1)
                self.botones_casillas[f][c] = btn

        panel_lateral = tk.Frame(contenedor, padx=10)
        panel_lateral.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.lbl_turno = tk.Label(
            panel_lateral, 
            text="Turno: Blancas ♔", 
            font=("Arial", 12, "bold"), 
            fg="#27ae60"
        )
        self.lbl_turno.pack(anchor="w", pady=10)

        lbl_hist = tk.Label(
            panel_lateral, 
            text="Historial de Movimientos:", 
            font=("Arial", 10, "bold")
        )
        lbl_hist.pack(anchor="w", pady=5)

        self.txt_historial = tk.Text(
            panel_lateral, 
            width=30, 
            height=18, 
            font=("Courier", 9), 
            state=tk.DISABLED
        )
        self.txt_historial.pack(fill=tk.BOTH, expand=True, pady=5)

        btn_reiniciar = tk.Button(
            panel_lateral, 
            text="Reiniciar Partida", 
            bg="#e74c3c", 
            fg="white", 
            font=("Arial", 10, "bold"), 
            command=self.reiniciar_partida
        )
        btn_reiniciar.pack(fill=tk.X, pady=10)

    def actualizar_tablero_visual(self):
        tablero = self.juego.tablero
        for f in range(8):
            for c in range(8):
                pieza = tablero.obtener_pieza(f, c)
                simbolo = pieza.obtener_simbolo() if pieza else ""
                color_fondo = "#f0d9b5" if (f + c) % 2 == 0 else "#b58863"
                self.botones_casillas[f][c].config(
                    text=simbolo, bg=color_fondo
                )

        turno_texto = "Blancas ♔" if self.juego.turno_actual == "blanco" else "Negras ♟"
        self.lbl_turno.config(text=f"Turno: {turno_texto}")

        self.txt_historial.config(state=tk.NORMAL)
        self.txt_historial.delete("1.0", tk.END)
        for mov in self.juego.obtener_historial():
            self.txt_historial.insert(tk.END, f"- {mov}\n")
        self.txt_historial.config(state=tk.DISABLED)

    def clic_casilla(self, fila, col):
        tablero = self.juego.tablero
        
        if self.origen_seleccionado is None:
            pieza = tablero.obtener_pieza(fila, col)
            if pieza and pieza.color == self.juego.turno_actual:
                self.origen_seleccionado = (fila, col)
                self.botones_casillas[fila][col].config(bg="#769656")
        else:
            if self.origen_seleccionado == (fila, col):
                self.origen_seleccionado = None
                self.actualizar_tablero_visual()
                return

            destino = (fila, col)
            resultado = self.juego.ejecutar_movimiento(self.origen_seleccionado, destino)
            
            self.origen_seleccionado = None
            
            if resultado == "victoria":
                self.actualizar_tablero_visual()
                ganador = "Blancas" if self.juego.turno_actual == "blanco" else "Negras"
                messagebox.showinfo("Fin del Juego", f"¡Jaque Mate! Victoria para las {ganador}.")
                self.reiniciar_partida()
            elif resultado is True:
                self.actualizar_tablero_visual()
            else:
                messagebox.showwarning("Movimiento Inválido", "La jugada seleccionada no cumple con las reglas de la pieza.")
                self.actualizar_tablero_visual()

    def reiniciar_partida(self):
        self.juego.reiniciar()
        self.origen_seleccionado = None
        self.actualizar_tablero_visual()
        