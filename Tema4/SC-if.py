# -*- coding: utf-8 -*-

"""
Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
Pista: Los números inferiores a 0 son negativos y los superiores, positivos.
"""


def main():
    numeroif: int = 0

    if numeroif < 0:
        print("El numero es Negativo")
    elif numeroif == 0:
        print("El numero es Cero")
    else:
        print("El numero es Positivo")


if __name__ == "__main__":
    main()
