# Autor: Enrique Martín
# Solución al ejercicio 8 (Posiciones de un caballo) de la hoja de ejercicios 
# sobre condionales

from typing import Tuple


# Función que calcula si una casilla está dentro del tablero
# Parámetros:
#   * casilla: Tuple[str, int]: pareja con la columna (rango 'a'-'h') y 
#     la fila (rango 1-8)
# Devuelve:
#   * bool: si la casilla está dentro del tablero
def casilla_valida(casilla: Tuple[str, int]) -> bool:
    columna: str = casilla[0]
    fila: int = casilla[1]
    return ('a' <= columna <= 'h') and (1 <= fila <= 8)


# Función que dada una casilla y un desplazamiento, calcula la casilla destino
# Parámetros:
#   * casilla: Tuple[str, int]: pareja con la columna (rango 'a'-'h') y 
#     la fila (rango 1-8)
#   * desplazamiento: Tuple[int, int]: pareja con el número de columnas y 
#     filas a desplazar (en ese orden)
# Devuelve:
#   * Tuple[str, int]: casilla destino después de desplazarse desde la casilla
#     inicial usando el desplazamiento
def mueve_casilla(casilla: Tuple[str, int], desplazamiento: Tuple[int, int]) -> Tuple[str, int]:
    nueva_c: str = chr(ord(casilla[0]) + desplazamiento[0])
    nueva_f: int = casilla[1] + desplazamiento[1]
    return nueva_c, nueva_f


# Función que calcula la casilla destino desde una original aplicando un desplazamiento, y
# la muestra por pantalla si
# dicha casilla destino está dentro del tablero
# Parámetros:
#   * casilla: Tuple[str, int]: pareja con la columna (rango 'a'-'h') y
#     la fila (rango 1-8)
#   * desplazamiento: Tuple[int, int]: pareja con el número de columnas y filas a
#     desplazar (en ese orden)
# Devuelve:
#   * None: no devuelve nada, solo muestra la casilla destino por pantalla si está dentro del tablero
def muestra_casilla_destino(casilla: Tuple[str, int], desplazamiento: Tuple[int, int]) -> None:
    destino: Tuple[str, int] = mueve_casilla(casilla, desplazamiento)
    if casilla_valida(destino):
        print(" -", destino)


# Función que comprueba todas los posibles movimientos de un caballo desde una casilla de origen,
# y muestra por pantalla aquellos que son válidos, es decir, están dentro del tablero
# Parámetros:
#   * casilla: Tuple[str, int]: casilla inicial, pareja con la columna (rango 'a'-'h')
#     y la fila (rango 1-8)
# Devuelve:
#   * None: no devuelve nada, solo muestra las casillas válidas a las que se puede mover un caballo
def muestra_casillas_caballo(casilla: Tuple[str, int]) -> None:
    print("Casillas posibles desde", casilla)
    # NOTA: esto se simplificará mucho cuando sepamos usar bucles
    muestra_casilla_destino(casilla, (1, 2))
    muestra_casilla_destino(casilla, (2, 1))
    muestra_casilla_destino(casilla, (2, -1))
    muestra_casilla_destino(casilla, (1, -2))
    muestra_casilla_destino(casilla, (-1, -2))
    muestra_casilla_destino(casilla, (-2, -1))
    muestra_casilla_destino(casilla, (-2, 1))
    muestra_casilla_destino(casilla, (-1, 2))
    print()


# Función principal para probar las funciones con distintos valores
# Parámetros:
#   * Ninguno
# Devuelve:
#   * None
def main() -> None:
    muestra_casillas_caballo(('f', 4))  # Casilla centrada
    muestra_casillas_caballo(('a', 1))  # Casilla en esquina inferior-izquierda
    muestra_casillas_caballo(('e', 1))  # Casilla en borde inferior


# Esto lo tenéis que poner siempre así sin cambiar nada
if __name__ == "__main__":
    main()
