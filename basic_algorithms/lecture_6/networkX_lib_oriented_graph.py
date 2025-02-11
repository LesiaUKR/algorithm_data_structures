import networkx as nx

# створюємо орієнтований граф DG
DG = nx.DiGraph()
DG.add_edge("A", "B") # Додаємо ребро від вершини A до вершини B
DG.add_edge("B", "A") # Додаємо ребро від вершини B до вершини A

G = nx.Graph()
G.add_edges_from([("A", "B"), ("B", "C")])
DG = nx.DiGraph(G) # Перетворюємо неорієнтований граф G в орієнтований граф DG
print("Орієнтований граф", DG)
print(DG.edges(), DG.nodes())