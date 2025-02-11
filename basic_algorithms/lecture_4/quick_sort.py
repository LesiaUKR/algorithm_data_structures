# Quicksort - обирається опорний елемент, розбиває масив на дві частини,
# одна з яких містить елементи менші за опорний, а інша - більші.
# головне - вибір опорного елементу
# Часова складність — логарифмічна O(n⋅logn) у середньому випадку, але 
# квадратична O(n^2) у найгіршому випадку

# Реалізація алгоритму Quicksort на Python з використанням рекурсії
def quicksort_recursion(arr):
    # Базовий випадок рекурсії: якщо масив порожній або має один елемент, він вже відсортований
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Вибираємо середній елемент як опорний (pivot)
    left = [x for x in arr if x < pivot] # Всі елементи, менші за опорний, додаємо до списку left
    middle = [x for x in arr if x == pivot] # Всі елементи, рівні опорному, додаємо до списку middle
    right = [x for x in arr if x > pivot] # Всі елементи, більші за опорний, додаємо до списку right
    return quicksort_recursion(left) + middle + quicksort_recursion(right) # Рекурсивно сортуємо left і right та об'єднуємо з middle

# Реалізація алгоритму Quicksort на Python з використанням циклів
def quicksort_loops(arr):
    if len(arr) <= 1:
        return arr

    # Створюємо стек для зберігання кортежів (left, right)
    stack = [(0, len(arr) - 1)]
    
    while stack:
        left, right = stack.pop()
        if left >= right:
            continue
        
        pivot = arr[right]  # Опорний елемент - останній елемент у поточному підмасиві
        i = left - 1
        
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        pivot_idx = i + 1
        
        stack.append((left, pivot_idx - 1))  # Додаємо ліву частину підмасиву до стеку
        stack.append((pivot_idx + 1, right))  # Додаємо праву частину підмасиву до стеку
    
    return arr

if __name__ == "__main__":
   numbers = [7, 12, 3, 5, 8, 11, 20, 1, 6, 14]
   print(numbers, quicksort_loops(numbers))