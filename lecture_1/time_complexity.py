# 1. O(1) - Алгоритм із часовою складністю O(1) — це константний час.
# Функція get_first_item просто повертає перше число списку.
# У нас завжди виконується одна операція, незалежно від розміру списку.
def get_first_item(items):
    return items[4]
# Завжди виконується одна операція, незалежно від розміру списку


print(get_first_item([1, 2, 3, 4, 5]))


#  2. O(n) - Алгоритм із часовою складністю просто проходить по списку чисел і друкує кожне число
# список з 10 числами, алгоритм виконає 10 операцій, а якщо список містить 1000 чисел — алгоритм виконає 1000 операцій

def print_all_items(items):
    for item in items:
        print(item)
# Кількість операцій прямо пропорційна кількості елементів у списку


print_all_items([1, 2, 3, 4, 5])


# 3. O(n^2) - Алгоритм із часовою складністю O(n^2) — це алгоритм, який має вкладені цикли.
# порівняння всіх пар векторів у списку, для перевірки того, чи є вони ортогональні
# вектори вважаються ортогональними, якщо їх скалярний добуток дорівнює нулю

def dot_product(v1, v2):

    return sum(x*y for x, y in zip(v1, v2))

def get_orthogonal_pairs(vectors):


    n = len(vectors)
    orthogonal_pairs = []

    for i in range(n):
        for j in range(i+1, n):
            if dot_product(vectors[i], vectors[j]) == 0:
                orthogonal_pairs.append((i, j))
    return orthogonal_pairs

vectors = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 1, 1]]
print(get_orthogonal_pairs(vectors))


# 4. O(n^3) - Алгоритм із часовою складністю O(n^3) — це алгоритм, який має три вкладені цикли.
# прикладом алгоритму з часовою складністю є множення матриць

def multiply_matrices(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]

    return C

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]

print(multiply_matrices(A, B))


# O(1) завжди буде найшвидшою складністю, оскільки вона не залежить від розміру вхідних даних.
# O(n) зростає лінійно, тому алгоритми з такою складністю будуть працювати добре для великих 
# розмірів вхідних даних порівняно з квадратичними або кубічними алгоритмами.
# O(n^2) та O(n^3) зростають значно швидше, особливо при великих розмірах вхідних даних. 
# Це означає, що алгоритми з такими складностями можуть стати непридатними для дуже великих наборів даних.