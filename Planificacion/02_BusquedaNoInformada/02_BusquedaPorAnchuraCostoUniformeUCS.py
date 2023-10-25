"""
La UCS es un algoritmo que ayuda a encontrar la ruta más corta en un mapa.
Comienza en un punto, como tu ubicación actual, y luego mira a su alrededor para
ver a dónde puedes llegar más rápido. Luego, se mueve a ese lugar y repite el
proceso. Continúa haciendo esto hasta llegar a tu destino.

UCS presta atención a cuánto cuesta llegar a cada lugar y siempre se mueve hacia
el lugar más barato en términos de tiempo o distancia. 
"""

import heapq

def ucs(graph, start, goal):
    visited = set()
    priority_queue = [(0, start)]  # Cola de prioridad con el costo acumulado y el nodo actual
    while priority_queue:
        (cost, node) = heapq.heappop(priority_queue)

        if node in visited:
            continue  # Saltar nodos ya visitados

        visited.add(node)

        if node == goal:
            return cost  # Se encontró la ruta más corta

        for neighbor, neighbor_cost in graph[node]:
            if neighbor not in visited:
                total_cost = cost + neighbor_cost
                heapq.heappush(priority_queue, (total_cost, neighbor))

    return float('inf')  # Si no se encuentra una ruta, retornar infinito

# Ejemplo de un grafo ponderado representado como un diccionario
graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('D', 3), ('E', 1)],
    'C': [('A', 5), ('F', 4)],
    'D': [('B', 3)],
    'E': [('B', 1), ('F', 7)],
    'F': [('C', 4), ('E', 7)]
}

start_node = 'A'
goal_node = 'F'

shortest_path_cost = ucs(graph, start_node, goal_node)

if shortest_path_cost != float('inf'):
    print(f"El costo de la ruta más corta desde {start_node} a {goal_node} es {shortest_path_cost}.")
else:
    print(f"No se encontró una ruta desde {start_node} a {goal_node}.")
