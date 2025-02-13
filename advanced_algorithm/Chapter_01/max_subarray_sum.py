def max_crossing_sum(arr, left, mid, right):
    # Ініціалізуємо ліву суму як мінус нескінченність для пошуку максимальної суми в лівій частині
    left_sum = float("-inf")
    total = 0  # Змінна для накопичення суми
    max_left = mid  # Відстежуємо ліву межу максимального перехідного підмасиву

    # Проходимо від середини до лівої межі, щоб знайти максимальну суму
    for i in range(mid, left - 1, -1):
        total += arr[i]
        if total > left_sum:
            left_sum = total
            max_left = i  # Оновлюємо ліву межу підмасиву

    # Ініціалізуємо праву суму як мінус нескінченність для пошуку максимальної суми в правій частині
    right_sum = float("-inf")
    total = 0  # Скидаємо total для обчислення правої частини
    max_right = mid + 1  # Відстежуємо праву межу максимального перехідного підмасиву

    # Проходимо від середини+1 до правої межі, щоб знайти максимальну суму
    for i in range(mid + 1, right + 1):
        total += arr[i]
        if total > right_sum:
            right_sum = total
            max_right = i  # Оновлюємо праву межу підмасиву

    # Повертаємо загальну максимальну суму перехідного підмасиву разом з межами
    return left_sum + right_sum, max_left, max_right


def max_subarray_sum(arr, left, right):
    # Базовий випадок: якщо є лише один елемент, повертаємо його
    if left == right:
        return arr[left], left, right

    # Знаходимо середній індекс масиву
    mid = (left + right) // 2

    # Рекурсивно знаходимо максимальну суму підмасиву в лівій частині
    left_sum, left_start, left_end = max_subarray_sum(arr, left, mid)

    # Рекурсивно знаходимо максимальну суму підмасиву в правій частині
    right_sum, right_start, right_end = max_subarray_sum(arr, mid + 1, right)

    # Знаходимо максимальну суму перехідного підмасиву, що охоплює обидві частини
    cross_sum, cross_start, cross_end = max_crossing_sum(arr, left, mid, right)

    # Визначаємо, який з трьох випадків (лівий, правий, перехідний) має максимальну суму
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_sum, left_start, left_end  # Лівий підмасив має максимальну суму
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_sum, right_start, right_end  # Правий підмасив має максимальну суму
    else:
        return cross_sum, cross_start, cross_end  # Перехідний підмасив має максимальну суму


# Приклад використання
arr = [2, -4, 1, 9, -6, 7, -3]
# Викликаємо функцію для знаходження максимальної суми підмасиву та його меж
max_sum, start, end = max_subarray_sum(arr, 0, len(arr) - 1)

# Виводимо результати
print(f"Максимальна сума підмасиву: {max_sum}")  # Виводимо максимальну суму
print(
    f"Підмасив: {arr[start:end + 1]}")  # Виводимо підмасив з максимальною сумою
