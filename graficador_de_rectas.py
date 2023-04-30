import matplotlib.pyplot as plt
import numpy as np
from shapely.geometry import LineString, Point
from probando import test
import ast


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

    print(len(lineas))
    interseccines = []

    for i in range(0, len(lineas)):
        for j in range(1, len(lineas)):
            interseccion = lineas[i].intersection(lineas[j])
            if type(interseccion) == Point:
                interseccines.append(interseccion)

    interseccines = list(set(interseccines))

    m = []
    n = []

    for interseccion in interseccines:
        xi, yi = interseccion.xy
        xi1 = np.float64(np.array(xi))
        yi1 = np.float64(np.array(yi))
        if validar_restriccion(restricciones, xi1, yi1):
            m.append(xi1)
            n.append(yi1)

    print(m)
    print(n)
    plt.fill(m, n, color='silver')

    """"
    [0.0, 3.0, 2.0, 4.0, 0.0, 0.0]
    [0.0, 0.0, 2.0, 0.0, 4.0, 6.0]
    combinacion con la que imprime correctamente la region factible
    """


def validar_restriccion(restricciones: list, x: int or float, y: int or float):
    for restriccion in restricciones:

        resultado = eval(f'{restriccion[0]}*{x} + {restriccion[1]}*{y} {restriccion[2]} {restriccion[3]}')
        if resultado == False:
            return False
    return True
