from optimzador_de_funcion import optimizar_funcion
from graficador_de_rectas import graficar_rectas

# coeficientes
label_fo = 'Z = 2x1 + 3.8x2'
coeficientes_funcion_objetivo = [2, 3.8, label_fo]

label_r1 = "1*x1 <= 20"
coeficientes_restriccion1 = [1, 0, '<=', 20, label_r1]

label_r2 = "1*x2 >= 14"
coeficientes_restriccion2 = [0, 1, '>=', 14, label_r2]

label_r3 = "50*x1 + 100*x2 == 1500"
coeficientes_restriccion3 = [50, 100, '==', 1500, label_r3]

restricciones = \
    [
        coeficientes_restriccion1,
        coeficientes_restriccion2,
        coeficientes_restriccion3
    ]





# si maximizar es True se maximiza la funcion objetivo, si es False se minimiza la funcion objetivo
maximizar: bool = False

solucion_z = optimizar_funcion(coeficientes_funcion_objetivo, maximizar, restricciones)

graficar_rectas(coeficientes_funcion_objetivo, solucion_z, restricciones)
