from optimzador_de_funcion import optimizar_funcion
from graficador_de_rectas import graficar_rectas

# coeficientes
label_fo = 'Z = 24x1 + 18x2'
coeficientes_funcion_objetivo = [24, 18, label_fo]

label_r1 = "300*x1 + 400*x2 <= 100000"
coeficientes_restriccion1 = [300, 400, '<=', 100000, label_r1]

label_r2 = "500*x1 + 200*x2 <= 120000"
coeficientes_restriccion2 = [500, 200, '<=', 120000, label_r2]

label_r3 = "200*x1 + 400*x2 <= 100000"
coeficientes_restriccion3 = [200, 400, '<=', 100000, label_r3]

label_r4 = "1*x2 >= 275"
coeficientes_restriccion4 = [0, 1, '>=', 275, label_r4]

restricciones = \
    [
        coeficientes_restriccion1,
        coeficientes_restriccion2,
        coeficientes_restriccion3,
        coeficientes_restriccion4
    ]

# si maximizar es True se maximiza la funcion objetivo, si es False se minimiza la funcion objetivo
maximizar: bool = False

solucion_z = optimizar_funcion(coeficientes_funcion_objetivo, maximizar, restricciones)

set_largo_eje_x = (0, 500)
set_largo_eje_y = (0, 700)
graficar_rectas(coeficientes_funcion_objetivo, solucion_z, restricciones, set_largo_eje_x, set_largo_eje_y)

