"""
 La búsqueda tabú comienza desde un punto aleatorio y explora vecinos cercanos.
 Se evitan movimientos repetitivos utilizando una lista tabú.
 La búsqueda continúa durante un número máximo de iteraciones (max_iter).

"""

import random

# Función de evaluación (puede variar según el problema)
def eval_func(x, y): #en este caso  busca maximizar un valor negativo
    return -(x**2 + y**2)  # Objetivo: maximizar el valor negativo

def generar_vecino(solucion, rango):
    x, y = solucion
    nuevo_x = x + random.uniform(-rango, rango)
    nuevo_y = y + random.uniform(-rango, rango)
    return nuevo_x, nuevo_y

def busqueda_tabu(max_iter, tam_tabu, rango):
    mejor_solucion = (0, 0)
    mejor_valor = eval_func(*mejor_solucion)
    solucion_actual = mejor_solucion
    lista_tabu = []

    for _ in range(max_iter):
        vecino = generar_vecino(solucion_actual, rango)

        if vecino in lista_tabu:
            continue  # Evitar movimientos tabú

        valor_vecino = eval_func(*vecino)

        if valor_vecino > mejor_valor:
            mejor_solucion = vecino
            mejor_valor = valor_vecino

        solucion_actual = vecino
        lista_tabu.append(vecino)

        if len(lista_tabu) > tam_tabu:
            lista_tabu.pop(0)  # Eliminar el movimiento tabú más antiguo

    return mejor_solucion, mejor_valor

# Ejecutar la búsqueda tabú
max_iter = 100
tam_tabu = 10
rango = 0.1

mejor_solucion, mejor_valor = busqueda_tabu(max_iter, tam_tabu, rango)

print(f"Mejor solución encontrada: {mejor_solucion}")
print(f"Valor de la función de evaluación: {mejor_valor}")

