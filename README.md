# Tablero de Ajedrez Simplificado en Python (POO)

Aplicación de escritorio interactiva desarrollada en Python utilizando Programación Orientada a Objetos y la biblioteca gráfica nativa `tkinter`. Permite jugar una partida de ajedrez básico respetando turnos, validando movimientos por tipo de pieza y mostrando un historial de jugadas en tiempo real.

---

## 1. Descripción del Problema
Muchas herramientas de aprendizaje de programación orientada a objetos se limitan a ejemplos abstractos en consola. Este proyecto busca llevar los principios avanzados de POO (como herencia, polimorfismo, abstracción y encapsulamiento) a un sistema interactivo visual y entretenido, facilitando la comprensión de cómo interactúan las clases, tableros y piezas en un entorno gráfico.

## 2. Objetivos
- Diseñar e implementar una arquitectura de software orientada a objetos en Python.
- Aplicar herencia y clases abstractas para modelar el comportamiento único de cada pieza de ajedrez.
- Desarrollar una interfaz gráfica intuitiva basada en eventos utilizando `tkinter`.
- Registrar el historial de movimientos y gestionar los turnos de la partida de forma robusta.

## 3. Funcionalidades Principales
1. **Validación de Movimientos por Pieza:** Cada pieza (Torre, Alfil, Reina, Rey, Caballo, Peón) valida de forma autónoma sus reglas de desplazamiento legal.
2. **Control de Turnos e Historial:** Alterna estrictamente entre jugadores (Blancas y Negras) y registra cada jugada válida en un panel lateral.
3. **Detección de Fin de Partida y Reinicio:** Detecta la captura del Rey (Jaque Mate) y permite reiniciar el tablero en cualquier momento con un botón de control.

## 4. Tecnologías Utilizadas
- **Lenguaje:** Python 3.10+
- **Interfaz Gráfica:** `tkinter` (Biblioteca nativa de Python)
- **Paradigma:** Programación Orientada a Objetos (POO)

## 5. Instrucciones de Instalación y Ejecución
1. Asegúrate de tener Python instalado en tu sistema.
2. Clona este repositorio o descarga los archivos fuente.
3. Ejecuta la aplicación desde la terminal en la raíz del proyecto:
   ```bash
   python main.py