"""
En la búsqueda en profundidad limitada se tiene un limite en cuanto puedes
avanzar en una direccion.

Comienzas en un punto.
Sigues un camino, pero solo avanzas hasta cierta distancia o profundidad.
Cuando alcanzas ese límite, retrocedes y exploras otro camino.
Repites esto hasta que hayas explorado todo o encontrado lo que buscas,
sin ir demasiado profundo.

Es útil cuando quieres explorar un grafo en profundidad, pero no quieres
ir muy lejos en una sola dirección. 
"""

def dls(graph, node, goal, depth_limit):    #verifica si hay un camino entre el nodo de inicio y el nodo 
    if depth_limit < 0:                     #de destino dentro del límite de profundidad especificado.
        return False  # Alcanzamos el límite de profundidad sin encontrar el objetivo

    if node == goal:
        return True  # Se encontró el objetivo

    if depth_limit == 0:
        return False  # Llegamos al límite de profundidad sin encontrar el objetivo

    for neighbor in graph[node]:
        if dls(graph, neighbor, goal, depth_limit - 1):
            return True

    return False

# Ejemplo de un grafo representado como un diccionario
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
goal_node = 'F'
depth_limit = 2

found = dls(graph, start_node, goal_node, depth_limit)

if found:
    print(f"Se encontró un camino desde {start_node} a {goal_node} dentro del límite de profundidad {depth_limit}.")
else:
    print(f"No se encontró un camino desde {start_node} a {goal_node} dentro del límite de profundidad {depth_limit}.")
