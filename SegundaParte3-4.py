
# -*- coding: utf-8 -*-

"""
Segunda parte:
Crear una clase coche.
Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene.
Una función que incremente el número de puertas que tiene el coche.
Crear un objeto miCoche en el main y añadirle una puerta.
Mostrar el número de puertas que tiene el objeto.
"""


def main():
    micoche: Coche = Coche()
    micoche.addpuerta()
    micoche.addpuerta()
    micoche.addpuerta()
    micoche.addpuerta()
    print(micoche.puertas)


class Coche:
    puertas: int = 0

    def addpuerta(self):
        Coche.puertas = Coche.puertas + 1
        #print(Coche().puertas)


if __name__ == '__main__':
    main()

