import networkx as nx

# Створюємо неорієнтований граф G без петель і кратних ребер
G = nx.Graph()


G.add_node("A") # Додаємо вершину A
print(G.nodes(), G.edges())

G.add_nodes_from(["B", "C", "D","F"]) # Додаємо вершини B, C, D
print(G.nodes(), G.edges())

G.add_edge("A", "B") # Додаємо ребро між вершинами A та B
print(G.nodes(), G.edges())

G.add_edges_from([("A", "B"), ("A", "C"), ("B", "C"), ("B", "D")]) # Додаємо ребра між вершинами A-C, B-C, B-D
print(G.nodes(), G.edges())

# Виводимо сусідні вершини для вершини "A"
print(list(G.neighbors("A")))  # ['B', 'C']

G.remove_node("F") # Видаляємо вершину F
# G.remove_nodes_from(["B", "C"]) # Видаляємо вершини B, C
print(G.nodes(), G.edges())

G.remove_edge("A", "B") # Видаляємо ребро між вершинами A та B
G.remove_edges_from([("A", "C"), ("B", "D")]) # Видаляємо ребра між вершинами A-C, B-D
print("Вершини графа G", G.nodes(), "Ребра графа G", G.edges())

# створюємо з орієнтованого графа DG неорієнтований граф G
DG = nx.DiGraph()
DG.add_edges_from([("A", "B"), ("B", "C")])
Graph_2 = nx.Graph(DG)

Graph_2.add_node(1)
Graph_2.add_node("Якась вершина")
Graph_2.add_node((2, 3))
print("Graph_2 вершини:",Graph_2.nodes())

# додаткові атрибути, такі як вага, етикетка тощо
Graph_2.add_edge(1, "A", weight=2.5, label="connection")

# можна додати атрибути під час і після створення вузлів та ребер
Graph_2.nodes[1]["color"] = "red"
Graph_2.edges[1, "A"]["label"] = "bridge"

# які вершини сусідні з вершиною "A"
neighbors_of_A = Graph_2["A"] # {'B': {}, 'C': {}}

# щоб отримати інформацію про ребро між вершинами "A" та "B"
edge_info = Graph_2["A"]["B"]  # {}
print("Ребро між A та B", edge_info)

# дізнаємося значення конкретного атрибуту ребра
edge_weight = Graph_2["A"]["B"]["weight"]
 
# додамо атртбут name для графа
Graph_2.graph["name"] = "My Graph"

# додамо атрибут для вершини
Graph_2.nodes["A"]["color"] = "blue"

# додамо атрибут для ребра
Graph_2["A"]["B"]["weight"] = 5


G.add_node("A", color="red")
G.add_edge("A", "B", weight=4)
