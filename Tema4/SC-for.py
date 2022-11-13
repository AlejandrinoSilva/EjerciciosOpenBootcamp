# -*- coding: utf-8 -*-

"""
Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0
y su condición será que la variable sea igual o menor que 3, se irá incrementando
en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla.
"""


def main():
    numerofor: int = 0

    for numerofor in range(3):
        print(numerofor)


if __name__ == '__main__':
    main()
