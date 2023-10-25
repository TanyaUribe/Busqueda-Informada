"""
La principal característica de la búsqueda voraz primero el mejor es que elige el
nodo con el valor de heurística más bajo como siguiente nodo a expandir. En otras
palabras, siempre elige la opción que parece estar más cerca de la solución en
función de la heurística. Esto lo convierte en un algoritmo "codicioso", ya que
toma decisiones locales con la esperanza de encontrar una solución global.

es como tomar el camino que parece el más prometedor en función de una estimación,
incluso si no garantiza la mejor solución. Es rápido, pero a veces puede
equivocarse. Se utiliza en aplicaciones como GPS y juegos donde la velocidad es importante.

"""

import heapq

def greedy_best_first_search(graph, start, goal, heuristic):
    open_set = []  # Conjunto de nodos por explorar
    heapq.heappush(open_set, (heuristic(start, goal), start))  # Inicializa el conjunto con el nodo de inicio y su heurística
    came_from = {}  # Diccionario para rastrear el camino

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in graph[current]:
            if neighbor not in came_from:
                came_from[neighbor] = current
                heapq.heappush(open_set, (heuristic(neighbor, goal), neighbor))

    return None  # No se encontró un camino

def heuristic(node, goal):
    # Heurística (puede variar según el problema)
    # En este ejemplo, utilizamos la distancia en línea recta (distancia Euclidiana) entre los nodos.
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path

# Ejemplo de un grafo no ponderado representado como un diccionario
graph = {
    (0, 0): {(0, 1), (1, 0)},
    (0, 1): {(0, 0), (1, 1)},
    (1, 0): {(0, 0), (1, 1)},
    (1, 1): {(0, 1), (1, 0)}
}

start_node = (0, 0)
goal_node = (1, 1)

path = greedy_best_first_search(graph, start_node, goal_node, heuristic)

if path:
    print("Camino encontrado:", path)
else:
    print("No se encontró un camino.")
