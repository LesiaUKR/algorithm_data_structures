# задача пакування рюкзака

# У вас є рюкзак з обмеженою місткістю та набір предметів, 
# кожен з яких має певну масу та вартість. Мета — максимізувати загальну
# вартість предметів, які ви можете покласти в рюкзак, не перевищуючи при
# цьому максимально допустиму місткість рюкзака.

# Задачу можна розв'язати наступними способами:
# 1. Брутфорс (Brute-force - перебір всіх можливих комбінацій) - складність O(2^n), повний перебір
# 2. Жадібний алгоритм (Greedy algorithm) - складність O(n*log(n)), найкращий локальний вибір, але не завжди оптимальний
# 3. Динамічне програмування (Dynamic programming) - складність O(n*W) -  поліноміальний час виконання, 
# оптимальний вибір, але вимагає багато пам'яті


# Брутфорс реалізація
# часова складність алгоритму - експонційна O(2^n)
# Функція для обчислення максимальної вартості
def knapSack(W, wt, val, n):
    # Базовий випадок
    if n == 0 or W == 0:
        return 0

    # Якщо вага n-го предмета більше, ніж місткість рюкзака, то цей предмет не можна включити у рюкзак
    if wt[n - 1] > W:
          # Рекурсивний виклик без включення n-го предмета
        return knapSack(W, wt, val, n - 1)

    # Якщо n-ий предмет можна включити в рюкзак,
    # повертаємо максимум із двох можливостей:
    # 1. Включити n-ий предмет
    # 2. Не включати n-ий предмет
    else:
        return max(
            # Вартість включення n-го предмета плюс максимальна вартість для решти предметів
            val[n - 1] + knapSack(W - wt[n - 1], wt, val, n - 1),
             # Максимальна вартість без включення n-го предмета
            knapSack(W, wt, val, n - 1),
        )

# ваги та вартість предметів
value = [60, 100, 120]
weight = [10, 20, 30]
# місткість рюкзака
capacity = 50
# кількість предметів
n = len(value)
# викликаємо функцію
print(knapSack(capacity, weight, value, n))  # 220
