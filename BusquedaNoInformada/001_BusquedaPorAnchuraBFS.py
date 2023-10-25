#La busqueda por anchura o BFS es un algoritmo para explorar y buscar
#en estructuras de datos como arboles o grafos de manera ordenada.
#Comienza en un punto y se mieve gradualmente hacia afuera, explorando
#todos los vecinos antes de avanzar al siguiente nivel.
#Es útil para encontrar rutas mas cortas y solucionar problemas
#relacionados con la conectividad en gráficos.

from collections import deque

def bfs(graph, start):
    visited = set()  # Conjunto para llevar un registro de nodos visitados
    queue = deque()   # Cola para llevar un registro de nodos por visitar

    queue.append(start)
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)  # Puedes reemplazar esto con la operación que desees en el nodo

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Ejemplo de un grafo representado como un diccionario
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Recorrido BFS desde el nodo A:")
bfs(graph, 'A')
