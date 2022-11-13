# -*- coding: utf-8 -*-

"""
Por último, para el Switch, deberás crear la variable estación,
y distintos case para las cuatro estaciones del año.
Dependiendo del valor de la variable estación se deberá mandar
un mensaje por consola informando de la estación en la que está.
También habrá que poner un default para cuando el valor de la variable no sea una estación.
"""


def main():
    estacion: str = "primavera"
    # En python no existe SwitchCase por lo que se reemplaza por If anidados

    if estacion == "verano":
        print("Verano")
    elif estacion == "otoño":
        print("Otoño")
    elif estacion == "invierno":
        print("Invierno")
    elif estacion == "primavera":
        print("Primavera")
    else:
        print("No se ha encontrado esa estación")


if __name__ == '__main__':
    main()
