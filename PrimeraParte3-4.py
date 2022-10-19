# -*- coding: utf-8 -*-

"""
Crear una función con tres parámetros que sean números que se suman entre sí.
Llamar a la función en el main y darle valores.
"""

def main():
    a: int = 50
    b: int = 10
    c: int = 16
    resultado: int = suma(a, b, c)
    print(resultado)


def suma(num1, num2, num3):
    return num1 + num2 + num3


if __name__ == '__main__':
    main()