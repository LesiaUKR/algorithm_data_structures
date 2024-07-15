import networkx as nx
import matplotlib.pyplot as plt

G = nx.complete_graph(8)
pos = [[0, 1, 2], [3, 4], [5, 6, 7]]  # Вказує камери для розташування вершин
pos = nx.shell_layout(G, pos)
nx.draw(G, pos, with_labels=True)
plt.title("Shell Layout")
plt.show()
