"""
 los Problemas de Satisfacción de Restricciones (CSP) son un tipo de problema en la inteligencia artificial
 en el que tienes un conjunto de variables que deben tomar ciertos valores de un dominio y están sujetas a
 restricciones específicas.
 El objetivo es encontrar una asignación de valores a las variables que cumpla con todas las restricciones.

"""


#Restricciones:
#A debe ser mayor que B.
#C debe ser igual a A - 2.

from itertools import product

# Definición de dominio para las variables A, B y C (en este caso, enteros del 1 al 5)
dominio = {A: [1, 2, 3, 4, 5] for A in 'ABC'}

# Función que verifica si se satisfacen las restricciones
def restricciones_satisfechas(asignacion):
    A, B, C = asignacion['A'], asignacion['B'], asignacion['C']
    return A > B and C == A - 2

# Algoritmo de fuerza bruta para resolver el CSP
solucion_encontrada = False
for asignacion in product(*dominio.values()):
    asignacion_actual = dict(zip(dominio.keys(), asignacion))
    if restricciones_satisfechas(asignacion_actual):
        print("Solución encontrada:", asignacion_actual)
        solucion_encontrada = True
        break

if not solucion_encontrada:
    print("No se encontró una solución que satisfaga las restricciones.")

