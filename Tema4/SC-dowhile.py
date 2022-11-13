# -*- coding: utf-8 -*-

"""
Para el bucle Do While, deberás crear la misma estructura que en el While,
pero solo se debe ejecutar una vez.
"""


def main():
    numerowhile: int = 1

    # Emulamos do while en python
    while True:
        print(numerowhile)
        numerowhile = numerowhile + 1
        if numerowhile == 3:
            break


if __name__ == '__main__':
    main()
