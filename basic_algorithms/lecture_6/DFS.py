def dfs_recursive(graph, vertex, visited=None):
    """
    Perform a depth-first search (DFS) on a graph starting from a given vertex.

    Parameters:
    graph (dict): The graph represented as an adjacency list.
    vertex: The starting vertex for the DFS.
    visited (set, optional): A set of already visited vertices. Defaults to None.

    Returns:
    None
    """
    
    # Initialize the visited set if it's not provided
    if visited is None:
        visited = set()
    
    # Mark the current vertex as visited
    visited.add(vertex)
    
    # Print the current vertex (you can replace this with any other operation)
    print(vertex, end=' ')
    
    # Recur for all the vertices adjacent to this vertex
    for neighbor in graph[vertex]:
        # If the neighbor has not been visited, perform DFS on the neighbor
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

# Представлення графа за допомогою списку суміжності
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Виклик функції DFS
print(dfs_recursive(graph, 'A'))

def dfs_iterative(graph, start_vertex):
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]  
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()  
        if vertex not in visited:
            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(graph[vertex]))  

# Представлення графа за допомогою списку суміжності
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Виклик функції DFS

print(dfs_iterative(graph, 'A'))