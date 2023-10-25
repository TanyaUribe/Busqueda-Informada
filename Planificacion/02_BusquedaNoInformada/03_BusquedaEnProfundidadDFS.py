"""
La búsqueda en profundidad es como explorar un laberinto: comienzas en un punto
y sigues el camino más profundo que puedas encontrar antes de retroceder. Haces
esto hasta que hayas explorado todo el laberinto o encontrado lo que buscas.
Si llegas a un punto muerto (sin más caminos), retrocedes y exploras otro camino.
Repites esto hasta que hayas cubierto todo o hayas encontrado lo que buscas.

La búsqueda en profundidad utiliza una pila (como una pila de platos) o la
recursión para llevar un registro de dónde has estado. 
No siempre garantiza la solución más corta y puede quedarse atascada en bucles.
"""

def dfs(graph, node, visited):
    if node not in visited:
        print(node)  # Puedes reemplazar esto con la operación que desees en el nodo.
        visited.add(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)

# Ejemplo de un grafo representado como un diccionario
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited_nodes = set()

print("Recorrido DFS desde el nodo A:")
dfs(graph, 'A', visited_nodes)
