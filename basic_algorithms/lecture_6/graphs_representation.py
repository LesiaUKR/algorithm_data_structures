# граф - пара (V,E), де V — будь-яка множина, а E — множина пар елементів V. Ми називаємо 
# V множиною вершин (vertex set), а E — множиною ребер (edge set)

G = ({"A", "B", "C", "D"}, {("A", "B"), ("B", "C"), ("C", "A"), ("D", "A")})

# V — це множина {"A", "B", "C", "D"}
# E - множина кортежів {("A", "B"), ("B", "C"), ("C", "A"), ("D", "A")}

# Вершина — це елемент графа, який представляє об'єкт.
# Ребро — це елемент графа, який представляє зв'язок між двома вершинами.
# Ступінь вершини — це кількість ребер, які виходять з вершини.
# Сусіди вершини — це вершини, з якими вершина пов'язана ребрами.
# Кількість ребер — це загальна кількість ребер у графі.
# Орієнтований граф (орграф) — це граф, у якому ребра мають напрямок.
# Неорієнтований граф — це граф, у якому ребра не мають напряму.
# Розріджений граф — це граф, у якому мало ребер.
# Щільний граф — це граф, у якому багато ребер.

# Способи представлення графів
# 1. матриця суміжності
adj_matrix = [
    [0, 1, 0, 1],  # Вершина A
    [1, 0, 1, 0],  # Вершина B
    [0, 1, 0, 1],  # Вершина C
    [1, 0, 1, 0]   # Вершина D
]

is_edge_AB = adj_matrix[0][1] # A відповідає першому рядку (індекс 0), а вершина B відповідає другому стовпчику (індекс 1)
# print(is_edge_AB)  # Це виведе 1, що означає, що ребро між A і B існує

is_edge_CD = adj_matrix[2][3] # C відповідає третьому рядку (індекс 2), а вершина D відповідає четвертому стовпчику (індекс 3)
# print(is_edge_CD)  # Це виведе 1, що означає, що ребро між C і D існує

# Напишіть функцію, яка приймає матрицю суміжності та повертає 1, 
# якщо існує ребро між конкретними вузлами,
# і -1, якщо такого ребра не існує. Вузли можна задавати індексами.

def is_edge(adj_matrix, node1, node2):
    if node1 >= len(adj_matrix) or node2 >= len(adj_matrix):
        return print(-1, "Вузол виходить за межі матриці")
    if adj_matrix[node1][node2] == 0:
        return print(0,  "Немає ребра між вузлами")
    return adj_matrix[node1][node2]  # Є ребро між вузлами
is_edge_DC = is_edge(adj_matrix, 3, 2)
print(f"Edge between D and C: {is_edge_DC}")


# 2. список суміжності - ефективніший з точки зору пам'яті спосіб представлення графа
# повільніший, наприклад, при перевірці наявності ребра між двома вершинами
adj_list = {
    'A': ['B', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'D'],
    'D': ['A', 'C']
}

# ключ - вершина, значення - список сусідів
neighbors_A = adj_list['A']
print(neighbors_A)  # ['B', 'D']

# 3. список ребер

edges = [
    ('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'C')
]

# якщо орієетований граф, то порядок вершин важливий: ('A', 'B') і ('B', 'A') - різні ребра
# якщо неорієнтований граф, то порядок вершин не важливий: ('A', 'B') і ('B', 'A') - одне й те ж ребро

# 4. матриця інцидентності
# Стовпці матриці відповідають ребрам, рядки — вершинам. 
# Ненульове значення в клітинці матриці вказує на зв'язок між вершиною і ребром (їх інцидентність).
