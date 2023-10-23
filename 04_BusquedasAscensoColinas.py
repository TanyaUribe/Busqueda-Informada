"""
es una técnica de búsqueda local que busca la mejor solución explorando los vecinos de un
punto inicial y eligiendo el vecino con el mejor valor (según una función de evaluación).
El proceso se repite hasta que no se encuentre un vecino mejor o se alcance un máximo local 

"""

import random

# Función de evaluación (puede variar según el problema)
def eval_func(x):
    return -x**2  # Objetivo: maximizar el valor negativo

def hill_climbing(max_iterations):
    current_solution = random.uniform(-10, 10)  # Punto de inicio aleatorio
    current_value = eval_func(current_solution)

    for _ in range(max_iterations):
        neighbor = current_solution + random.uniform(-0.1, 0.1)  # Generar vecino cercano
        neighbor_value = eval_func(neighbor)

        if neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value

    return current_solution, current_value

# Ejecutar la búsqueda de ascenso de colinas
max_iterations = 100
best_solution, best_value = hill_climbing(max_iterations)

print(f"Mejor solución encontrada: {best_solution}")
print(f"Valor de la función de evaluación: {best_value}")

"""
Este código busca la mejor solución en una función sencilla que busca
maximizar un valor negativo. Comienza desde un punto aleatorio y se mueve
a opciones cercanas si son mejores. La búsqueda se detiene después de un número
de iteraciones (max_iter) o cuando no se encuentra una solución mejor.
"""

