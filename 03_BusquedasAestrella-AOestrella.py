"""
A* encuentra la mejor solución si la estimación es precisa,
mientras que AO* se adapta a estimaciones menos precisas y
proporciona soluciones aproximadas. 

"""

import heapq

def a_star(graph, start, goal, heuristic):
    open_set = []  # Conjunto de nodos por explorar
    heapq.heappush(open_set, (0, start))  # Inicializa el conjunto con el nodo de inicio y su costo (0)
    came_from = {}  # Diccionario para rastrear el camino
    g_score = {node: float('inf') for node in graph}  # Costo real acumulado desde el nodo de inicio
    g_score[start] = 0  # El costo desde el inicio a sí mismo es 0

    while open_set:
        current = heapq.heappop(open_set)[1]

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))

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

# Ejemplo de un grafo ponderado representado como un diccionario
graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1}
}

start_node = (0, 0)
goal_node = (1, 1)

path = a_star(graph, start_node, goal_node, heuristic)

if path:
    print("Camino encontrado:", path)
else:
    print("No se encontró un camino.")
