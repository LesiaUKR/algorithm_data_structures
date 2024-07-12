
def linear_search(arr, x): # arr - масив\список, x - елемент, який потрібно знайти
   for i in range(len(arr)): # проходимо по кожному елементу масиву
      if arr[i] == x: # якщо елемент знайдено
         return i # повертаємо його індекс
   return -1 # якщо елемент не знайдено повертаємо -1

numbers = [1, 3, 5, 7, 9, 11]
print(linear_search(numbers, 7))  # Output: 3