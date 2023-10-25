"""
Combina la Búsqueda en Profundidad y la Búsqueda en Anchura.
Comienza con una exploración superficial.
Luego, aumenta gradualmente la profundidad de búsqueda.
Continúa hasta que encuentres la solución.

IDDFS es especialmente útil cuando no tienes información sobre la
profundidad de la solución o cuando la memoria es un recurso limitado. 
"""

def dfs(graph, node, goal, depth):
    if depth == 0:
        if node == goal:
            return True
        return False

    if depth > 0:
        for neighbor in graph[node]:
            if dfs(graph, neighbor, goal, depth - 1):
                return True
    return False

def iddfs(graph, start, goal):
    depth = 0
    while True:
        if dfs(graph, start, goal, depth):
            return True  # Se encontró una solución
        depth += 1

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

found = iddfs(graph, start_node, goal_node)

if found:
    print(f"Se encontró un camino desde {start_node} a {goal_node}.")
else:
    print(f"No se encontró un camino desde {start_node} a {goal_node}.")
