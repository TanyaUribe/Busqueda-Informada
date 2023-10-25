"""
Es utilizado para encontrar una solución o un camino entre dos puntos en un grafo,
árbol o estructura de datos jerárquica.

Comienzan desde lados opuestos simultpaneamente.
Ambos avanzan hacia el centro al mismo tiempo.
Si se encuentran en algún punto intermedio, se encontró la solución.
Si no se encuentran o llegan al punto en el que no pueden avanzar más, no hay solución.

"""

def bidirectional_search(graph, start, goal): #realiza la búsqueda desde ambos extremos y devuelve un mensaje cuando se encuentra una solución o cuando no se encuentra ninguna.
    forward_queue = [start]
    backward_queue = [goal]
    forward_visited = set()
    backward_visited = set()

    while forward_queue and backward_queue:
        # Búsqueda desde el nodo de inicio
        current_start = forward_queue.pop(0)
        forward_visited.add(current_start)

        # Búsqueda desde el nodo de destino
        current_goal = backward_queue.pop(0)
        backward_visited.add(current_goal)

        if current_start in backward_visited:
            return "Solución encontrada"  # Se encontraron en el medio

        if current_goal in forward_visited:
            return "Solución encontrada"  # Se encontraron en el medio

        for neighbor in graph[current_start]:
            if neighbor not in forward_visited:
                forward_queue.append(neighbor)

        for neighbor in graph[current_goal]:
            if neighbor not in backward_visited:
                backward_queue.append(neighbor)

    return "No se encontró una solución"

# Ejemplo de un grafo no ponderado representado como un diccionario
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
goal_node = 'F'

result = bidirectional_search(graph, start_node, goal_node)
print(result)
