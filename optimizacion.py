from optimzador_de_funcion import optimizar_funcion
from graficador_de_rectas import graficar_rectas

# coeficientes
label_fo = 'Z = 4x1 + 3x2'
coeficientes_funcion_objetivo = [4, 3, label_fo]

label_r1 = "1*x1 + 1*x2 <= 4"
coeficientes_restriccion1 = [1, 1, '<=', 4, label_r1]

label_r2 = "2*x1 + 1*x2 <= 6"
coeficientes_restriccion2 = [2, 1, '<=', 6, label_r2]

restricciones = \
    [
        coeficientes_restriccion1,
        coeficientes_restriccion2,
    ]

# si maximizar es True se maximiza la funcion objetivo, si es False se minimiza la funcion objetivo
maximizar: bool = True

solucion_z = optimizar_funcion(coeficientes_funcion_objetivo, maximizar, restricciones)

graficar_rectas(coeficientes_funcion_objetivo, solucion_z, restricciones)
