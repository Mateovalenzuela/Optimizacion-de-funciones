import pulp


def optimizar_funcion(funcion_objetivo: list, maximizar: bool, restricciones: list):
    # Definir las variables del problema
    x1 = pulp.LpVariable('x1', lowBound=0, cat='Continuous')
    x2 = pulp.LpVariable('x2', lowBound=0, cat='Continuous')

    # Definir el problema
    if maximizar:
        problem = pulp.LpProblem('Problema de maximización', pulp.LpMaximize)
    else:
        problem = pulp.LpProblem('Problema de maximización', pulp.LpMinimize)

    # Definir la función objetivo
    problem += (funcion_objetivo[0] * x1) + (funcion_objetivo[1] * x2)

    # Definir las restricciones
    for restriccion in restricciones:
        if restriccion[2] == '<=':
            problem += (restriccion[0] * x1) + (restriccion[1] * x2) <= restriccion[3]
        elif restriccion[2] == '>=':
            problem += (restriccion[0] * x1) + (restriccion[1] * x2) >= restriccion[3]
        elif restriccion[2] == '==':
            problem += (restriccion[0] * x1) + (restriccion[1] * x2) == restriccion[3]
        else:
            raise Exception(f'Error en el signo de la restriccion: {restriccion}')

    # Resolver el problema
    status = problem.solve()

    # guardar la solucion previa. sirve para analizar el tipo de solucion
    prev_sol = problem.objective.value()

    # soluciones
    solucion_x1 = pulp.value(x1)
    solucion_x2 = pulp.value(x2)
    solucion_z = pulp.value(problem.objective)

    # Verificar el estado de resolución del problema
    if pulp.LpStatus[status] == "Optimal":
        # Verificar si hay soluciones alternativas
        if abs(problem.objective.value() - prev_sol) != 0:
            print("Hay soluciones alternativas")
        else:
            print("La solución es única")

        # Imprimir la solución
        print('x1 =', solucion_x1)
        print('x2 =', solucion_x2)
        print('Z =', solucion_z)

    else:
        print("El problema no tiene solución")

    return solucion_z
