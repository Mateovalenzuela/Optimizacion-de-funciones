import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString, Point
import math


def graficar_rectas(funcion_objetivo: list, solucion_fo: float or int, restricciones: list):
    # Graficar las restricciones y la función objetivo
    fig, ax = plt.subplots()

    # grafica las restricciónes:
    for restriccion in restricciones:
        x1 = np.linspace(0, 5, 100)
        x2 = (restriccion[3] - (restriccion[0] * x1)) / restriccion[1]
        ax.plot(x1, x2, label=f'{restriccion[4]} (R1)')

    # grafica la F.O
    func_obj_x1 = np.linspace(0, 10, 100)
    func_obj_x2 = (solucion_fo - funcion_objetivo[0] * func_obj_x1) / funcion_objetivo[1]
    ax.plot(func_obj_x1, func_obj_x2, label=f'{funcion_objetivo[2]}', linestyle='--')

    graficar_region_factible(restricciones)

    ax.set_xlim([0, 6])
    ax.set_ylim([0, 6])
    ax.legend()
    plt.show()


def graficar_region_factible(restricciones: list):
    lineas = []
    x = np.linspace(0, 5, 100)
    y = np.arange(0, 150, 50)

    x1 = 0 * y
    y1 = 0 * x

    for restriccion in restricciones:
        x2 = (restriccion[3] - (restriccion[0] * x)) / restriccion[1]
        linea = LineString(np.column_stack((x, x2)))
        lineas.append(linea)

    lineas.append(LineString(np.column_stack((x1, y))))
    lineas.append(LineString(np.column_stack((x, y1))))

    interseccines = []

    for i in range(0, len(lineas)):
        for j in range(1, len(lineas)):
            interseccion = lineas[i].intersection(lineas[j])
            if type(interseccion) == Point:
                interseccines.append(interseccion)

    interseccines = list(set(interseccines))

    puntos = []
    for interseccion in interseccines:
        xi, yi = interseccion.xy
        xi1 = np.float64(np.array(xi))
        yi1 = np.float64(np.array(yi))
        if validar_restriccion(restricciones, xi1, yi1):
            puntos.append((xi1, yi1))

    puntos_ordenados = ordenar_puntos_en_sentido_antihorario(puntos)
    x = []
    y = []
    for punto in puntos_ordenados:
        x.append(punto[0])
        y.append(punto[1])

    plt.fill(x, y, color='silver')


def validar_restriccion(restricciones: list, x: int or float, y: int or float):
    for restriccion in restricciones:

        resultado = eval(f'{restriccion[0]}*{x} + {restriccion[1]}*{y} {restriccion[2]} {restriccion[3]}')
        if resultado == False:
            return False
    return True


def ordenar_puntos_en_sentido_antihorario(puntos):
    # Encontrar el punto más a la derecha
    punto_inicio = max(puntos, key=lambda punto: punto[0])

    def calcular_angulo_con_respecto_a_inicio(punto):
        x, y = punto[0] - punto_inicio[0], punto[1] - punto_inicio[1]
        return math.atan2(y, x)

    # Ordenar los puntos según su ángulo con respecto al punto de inicio
    puntos_ordenados = sorted(puntos, key=calcular_angulo_con_respecto_a_inicio)

    # Devolver los puntos en el orden que se han ordenado
    return puntos_ordenados
