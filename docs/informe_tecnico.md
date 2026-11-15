# Informe Técnico — Tablero de Ajedrez Simplificado

## 1. Análisis del Problema
Se identificó la necesidad de construir una aplicación de escritorio que combine lógica compleja de validación espacial (movimientos en tablero de 8x8) con una interfaz gráfica responsiva, aplicando de forma estricta los principios de la Programación Orientada a Objetos. El sistema está dirigido a entusiastas de los juegos de mesa y estudiantes que deseen estudiar la arquitectura limpia en Python.

## 2. Diseño Inicial
Se planificó dividir el software en tres capas principales:
- **Capa de Modelos:** Contiene las entidades del dominio (`Pieza`, `Torre`, `Alfil`, `Reina`, `Rey`, `Caballo`, `Peon`, `Tablero`, `Juego`).
- **Capa de Lógica / Servicios:** Administra el flujo de turnos, validación de jugadas y almacenamiento temporal en memoria del historial.
- **Capa de Interfaz:** Renderiza el tablero mediante botones cuadriculados y captura eventos de clic del usuario.

## 3. Arquitectura
Se estructuró el código bajo una separación clara de responsabilidades: los modelos de piezas desconocen la existencia de la interfaz gráfica (`tkinter`), y la interfaz únicamente invoca métodos de la clase `Juego` y `Tablero`, cumpliendo con los principios de bajo acoplamiento.

## 5. Aplicación de POO

| Concepto | Clase o Método | Archivo | Explicación |
| :--- | :--- | :--- | :--- |
| **Clases y objetos** | `Tablero`, `Juego`, `Pieza` | `pieza.py`, `tablero.py`, `juego.py` | Se instancian múltiples objetos que representan el estado actual de la partida y las fichas en el tablero. |
| **Encapsulamiento** | `_color`, `_fila`, `_columna`, `@property` | `pieza.py` | Se protegen los atributos internos de las piezas y se exponen mediante propiedades de lectura controlada. |
| **Herencia** | `Torre`, `Alfil`, `Reina`, etc. heredan de `Pieza` | `pieza.py` | Reutilizan los atributos base de posición y color, especializando su comportamiento. |
| **Polimorfismo** | `movivimientos_validos(tablero)` | `pieza.py` | Cada subclase implementa su propio algoritmo de movimiento respetando la misma firma de método. |
| **Abstracción** | `Pieza` (con `abc.ABC` y `@abstractmethod`) | `pieza.py` | Define un contrato obligatorio que toda pieza concreta debe implementar (`obtener_simbolo` y `movivimientos_validos`). |
| **Relaciones** | Composición (`Juego` contiene `Tablero`) | `juego.py`, `tablero.py` | El tablero es creado y destruido dentro del ciclo de vida del juego. |

## 6. Construcción de la Interfaz
Se utilizó **Tkinter**, la biblioteca estándar de Python, aprovechando su estabilidad y ausencia de dependencias externas pesadas. La interfaz está construida mediante una matriz de botones bidimensional (`8x8`) estilizada con colores alternados y caracteres Unicode (`♔`, `♕`, `♖`, etc.), comunicándose con la lógica mediante funciones callback (`clic_casilla`).

## 7. Proceso de Desarrollo
1. Definición de la clase abstracta `Pieza` y su jerarquía de herencia.
2. Implementación de la matriz en `Tablero` y posicionamiento inicial de fichas.
3. Desarrollo de la lógica de turnos y validación de movimientos en la clase `Juego`.
4. Construcción de la interfaz gráfica con `tkinter` y enlace de eventos de clic.
5. Pruebas de integración y refinamiento del historial de jugadas.

## 8. Pruebas

| Prueba | Acción realizada | Resultado esperado | Resultado obtenido |
| :--- | :--- | :--- | :--- |
| **Prueba 1** | Intentar mover un peón blanco en el turno de las negras. | El movimiento debe ser rechazado y advertir que no es el turno correspondiente. | Correcto: Se muestra advertencia y no se altera el tablero. |
| **Prueba 2** | Mover una torre blanca obstruida por sus propias piezas. | La torre no debe poder saltar piezas amigas. | Correcto: El método de validación restringe los casilleros libres. |
| **Prueba 3** | Capturar la pieza del Rey adversario. | Detectar el fin de partida, mostrar cartel de victoria y reiniciar. | Correcto: Mensaje de victoria desplegado y tablero reseteado. |

## 9. Problemas y Soluciones
1. **Dificultad en el cálculo de casillas intermedias para piezas deslizantes (Torre/Alfil):**  
   *Diagnóstico:* Las piezas podían atravesar otras fichas si no se detenía la iteración al encontrar un obstáculo.  
   *Solución:* Se implementó un bucle con condición de parada inmediata (`break`) al detectar la primera pieza ocupando una casilla en cada dirección.
2. **Actualización visual tras clics consecutivos:**  
   *Diagnóstico:* Al hacer clic en casillas vacías o inválidas, el estado de selección quedaba desincronizado.  
   *Solución:* Se añadió un método centralizado `actualizar_tablero_visual()` que refresca todos los botones y limpia las selecciones activas tras cada interacción.
