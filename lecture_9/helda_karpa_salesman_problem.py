# Алгоритм Хелда-Карпа для задачі комівояжера — це метод динамічного програмування, 
# що значно ефективніший за повний перебір, особливо для середніх і невеликих розмірів задач.
# Алгоритм Хелда-Карпа має час виконання O(n^2⋅2^n), який є поліноміальним відносно кількості міст 
# n, що є значним поліпшенням порівняно з факторіальним часом виконання повного перебору.
# Однак, через експоненціальний компонент у часовій складності, алгоритм Хелда-Карпа все ще 
# є непрактичним для дуже великих наборів даних.

from math import sqrt  # Імпортуємо функцію sqrt з модуля math для обчислення квадратного кореня.
from itertools import combinations  # Імпортуємо функцію combinations з модуля itertools для генерації комбінацій.

def held_karp(distance_matrix):
    n = len(distance_matrix)  # Визначаємо кількість міст на основі розміру матриці відстаней.

    # Ініціалізація таблиці динамічного програмування.
    # Використовуємо кортежі для представлення наборів міст.
    dp = {(frozenset([0, i]), i): (distance_matrix[0][i], [0, i]) for i in range(1, n)}

    # Встановлюємо базовий випадок - відстань від першого міста до себе дорівнює 0.
    dp[(frozenset([0]), 0)] = (0, [0])

    # Перебираємо підмножини зростаючого розміру і знаходимо мінімальну відстань до кінцевого міста.
    for r in range(2, n + 1):
        for subset in combinations(range(1, n), r):
            subset = frozenset(subset) | frozenset([0])  # Додаємо початкове місто до підмножини.
            for next_city in subset:
                if next_city == 0:  # Пропускаємо початкове місто.
                    continue
                prev_subset = subset - frozenset([next_city])  # Створюємо попередню підмножину без next_city.
                dp[(subset, next_city)] = min(
                    (
                        dp[(prev_subset, last_city)][0] + distance_matrix[last_city][next_city],  # Додаємо відстань.
                        dp[(prev_subset, last_city)][1] + [next_city]  # Оновлюємо шлях.
                    )
                    for last_city in prev_subset if last_city != 0  # Перебираємо всі попередні міста.
                )

    # Знаходимо мінімальну вартість, щоб завершити тур і повернутися до початкового міста.
    all_cities = frozenset(range(n))
    result = min(
        (
            dp[(all_cities, last_city)][0] + distance_matrix[last_city][0],  # Додаємо відстань повернення.
            dp[(all_cities, last_city)][1] + [0]  # Оновлюємо шлях.
        )
        for last_city in range(1, n)
    )

    return result  # Повертаємо мінімальну відстань і відповідний шлях.

# Функція для обчислення відстані між двома точками.
def calculate_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)  # Використовуємо формулу відстані.

if __name__ == '__main__':
    # Словник із координатами міст.
    cities = {"A": (0, 0), "B": (1, 5), "C": (2, 2), "D": (3, 3), "E": (5, 1)}

    # Створення матриці відстаней.
    distance_matrix = []
    for i, source in enumerate(cities.values()):
        distance_matrix.append([])  # Додаємо новий рядок для кожного міста.
        for target in cities.values():
            # Додавання розрахованої відстані до матриці.
            distance_matrix[i].append(calculate_distance(source, target))

    # Виклик функції алгоритму з матрицею відстаней.
    result, path = held_karp(distance_matrix)
    print(result, path)  # Виводимо результат: мінімальну відстань і шлях у вигляді індексів.

    # Переводимо шлях від індексів до назв міст.
    city_names = list(cities.keys())
    path_with_names = [city_names[i] for i in path]

    print(result, path_with_names)  # Виводимо результат: мінімальну відстань і шлях у вигляді назв міст.
