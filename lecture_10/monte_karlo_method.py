# Метод Монте-Карло — це статистичний алгоритм, який використовує випадковість та ймовірність
# для розв’язання різних проблем, які можуть бути складними або неможливими 
# для точного розв'язання традиційними методами. Основна ідея полягає в тому, 
# щоб використовувати випадкові зразки для апроксимації результатів.

# Метод Монте-Карло базується на Законі великих чисел, який стверджує, що середнє значення
# результатів великої кількості експериментів має тенденцію наближатися до очікуваного значення,
# коли кількість експериментів стає дуже великою.

import random  # Імпортуємо модуль random для генерації випадкових чисел

def is_inside(a, b, x, y):
    """Перевіряє, чи знаходиться точка (x, y) всередині трикутника."""
    return y <= (b / a) * x  # Перевіряємо, чи точка (x, y) знаходиться нижче або на прямій y = (b/a) * x

def monte_carlo_simulation(a, b, num_experiments):
    """Виконує серію експериментів методом Монте-Карло."""
    average_area = 0  # Ініціалізуємо змінну для накопичення площ

    for _ in range(num_experiments):
        # Генерація випадкових точок всередині прямокутника
        points = [(random.uniform(0, a), random.uniform(0, b)) for _ in range(15000)]
        # Відбір точок, що знаходяться всередині трикутника
        inside_points = [point for point in points if is_inside(a, b, point[0], point[1])]

        # Розрахунок площі трикутника за методом Монте-Карло
        M = len(inside_points)  # Кількість точок всередині трикутника
        N = len(points)  # Загальна кількість точок
        area = (M / N) * (a * b)  # Площа трикутника, обчислена методом Монте-Карло

        # Додавання до середньої площі
        average_area += area  # Накопичуємо площі для обчислення середнього

    # Обчислення середньої площі
    average_area /= num_experiments  # Ділимо на кількість експериментів, щоб отримати середнє значення
    return average_area  # Повертаємо середню площу

# Розміри прямокутника
a = 10  # Ширина прямокутника
b = 5  # Висота прямокутника
S = (a * b) / 2  # Теоретична площа трикутника (ширина * висота / 2)

# Кількість експериментів
num_experiments = 100  # Кількість повторень симуляції

# Виконання симуляції
average_area = monte_carlo_simulation(a, b, num_experiments)  # Запускаємо симуляцію
print(f"Теоретична площа трикутника: {S}")  # Виводимо теоретичну площу
print(f"Середня площа трикутника за {num_experiments} експериментів: {average_area}")  # Виводимо середню площу, отриману за допомогою методу Монте-Карло
