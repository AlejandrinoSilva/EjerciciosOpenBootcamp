# -*- coding: utf-8 -*-

"""
Crea un bucle While, este bucle tendrá que tener como condición que la
variable numeroWhile sea inferior a 3, el bloque de código que tendrá el bucle deberá:
- Incrementar el valor de la variable en uno cada vez que se ejecute.
- Mostrarlo por pantalla cada vez que se ejecute.
"""


def main():
    numerowhile: int = 1

    while numerowhile <= 3:
        print(numerowhile)
        numerowhile += numerowhile


if __name__ == '__main__':
    main()
