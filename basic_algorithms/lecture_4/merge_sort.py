# Merge sort - ділить масив на дві половини, сортує кожну з них і потім зливає їх разом
# Часова складність: Логарифмічно-лінійна/quazilinear O(n log n) у загальному випадку
# https://www.youtube.com/watch?v=3j0SWDX4AtU
# merge sort швидший ніж insertion sort, selection sort, bubble sort
# space complexity O(n) на відміну від bubble sort, insertion sort, selection sort для яких space complexity O(1)
# тобто якщо мердж сорт реалізовувати за допомогою рекурсії, то він потребує досить багато пам'яті
# але можна реалізувати merge sort без рекурсії, використовуючи цикли
# в такому випадку merge sort буде використовувати O(n) пам'яті
# в сучасних мовах програмування використовується Timsort - гібрид merge sort і insertion sort
# https://uk.wikipedia.org/wiki/Timsort
# sort та sorted в Python використовують Timsort
# sort - 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

# відповідає за сортування двох підмасивів
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднайте менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Якщо в лівій або правій половині залишилися елементи, 
		# додайте їх до результату
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

if __name__ == "__main__":
    numbers = [7, 12, 3, 5, 8, 11, 20, 1, 6, 14]
    print(numbers, merge_sort(numbers))
    # Виведе: [7, 12, 3, 5, 8, 11, 20, 1, 6, 14] [1, 3, 5, 6, 7, 8, 11, 12, 14, 20]
  
