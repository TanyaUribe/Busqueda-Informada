"""
La búsqueda de haz local es una técnica de búsqueda local que explora
varias soluciones cercanas al mismo tiempo y selecciona las mejores.
En este ejemplo, buscamos maximizar una función de evaluación simple.

"""

import random

# Función de evaluación (puede variar según el problema)
def eval_func(x):
    return -(x**2)  # Objetivo: maximizar el valor negativo

def generar_solucion():
    return random.uniform(-10, 10)  # Genera una solución aleatoria

def busqueda_haz_local(num_soluciones, max_iter):
    soluciones = [generar_solucion() for _ in range(num_soluciones)]

    for _ in range(max_iter):
        vecinos = [s + random.uniform(-0.1, 0.1) for s in soluciones]  # Genera vecinos cercanos
        soluciones = sorted(vecinos, key=lambda x: eval_func(x), reverse=True)[:num_soluciones]

    mejor_solucion = max(soluciones, key=lambda x: eval_func(x))
    mejor_valor = eval_func(mejor_solucion)

    return mejor_solucion, mejor_valor

# Ejecutar la búsqueda de haz local
num_soluciones = 10
max_iter = 100

mejor_solucion, mejor_valor = busqueda_haz_local(num_soluciones, max_iter)

print(f"Mejor solución encontrada: {mejor_solucion}")
print(f"Valor de la función de evaluación: {mejor_valor}")

"""
generamos un conjunto de soluciones iniciales aleatorias y las evaluamos
utilizando una función de evaluación. Luego, generamos vecinos cercanos
y seleccionamos las mejores soluciones.
Repetimos este proceso durante un número máximo de iteraciones (max_iter).
"""
