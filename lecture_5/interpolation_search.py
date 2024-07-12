# Інтерполяційний пошук - це покращення бінарного пошуку, на основі формули, яка 
# розраховує index елемента, який шукаємо — потенційне положення значення пошуку у списку — використовуючи лінійну інтерполяцію
# Масив повинен бути відсортованим
# Цей метод працює найкращим чином, коли ключі розподілені рівномірно.
# Якщо ключі розподілені нерівномірно, інтерполяційний пошук може працювати повільніше, ніж бінарний.
# найчастіше використовується в базах даних для пошуку рівномірно розподілених ключів

# Обмеження інтерполяційного пошуку:
# 1. Масив повинен бути відсортованим
# 2. Масив повинен бути рівномірно розподіленим

# Data structure	Array
# Worst-case performance	O(n)
# Best-case performance	O(1)
# Average performance	O(log(log(n)))
# Worst-case space complexity	O(1)

# базовий алгоритм інтерполяційного пошуку
def interpolation_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high and x >= arr[low] and x <= arr[high]:
        index = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))
        if arr[index] == x:
            return index
        if arr[index] < x:
            low = index + 1
        else:
            high = index - 1

    return -1

arr = [1, 3, 5, 7, 9, 11, 14, 16, 18, 20, 22, 25, 28, 30]
index = interpolation_search(arr, 25) # 11
print(index)
print(arr[index])  # 25
index = interpolation_search(arr, 22)
print(index) # 10
print(arr[index])