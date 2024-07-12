# Linear search -  O(n) time complexity
# працює з будь-яким масивом, незалежно від того, чи він впорядкований чи ні
# перевіряє кожен елемент масиву послідовно, починаючи з першого елементу, поки не знайде шуканий елемент
# Якщо елемент знайдено, повертає його індекс, в іншому випадку повертає -1
# працює зі списком або будь-якою ітерабельною структурою даних
# у середньому випадку, коли елемент може знаходитись на будь-якій позиції у списку, очікувана часова складність становить 
# O(n/2), що все ще лінійно
# Це робить лінійний пошук менш ефективним для великих впорядкованих даних, 
# де можуть бути використані ефективніші алгоритми, такі як двійковий пошук.

# шукаємо конкретний елемент у масиві
def linear_search(arr, x): # arr - масив\список, x - елемент, який потрібно знайти
   for i in range(len(arr)): # проходимо по кожному елементу масиву
      if arr[i] == x: # якщо елемент знайдено
         return i # повертаємо його індекс
   return -1 # якщо елемент не знайдено повертаємо -1

numbers = [1, 3, 5, 7, 9, 11]
print(linear_search(numbers, 7))  # Output: 3


# перевіряємо чи існує елемент у списку
def exists_in_list(arr, x):
    return linear_search(arr, x) != -1

numbers = [1, 3, 5, 7, 9, 11]
print(exists_in_list(numbers, 7))  # Output: True
print(exists_in_list(numbers, 2))  # Output: False

def exists_in_list_and_index(arr, x):
    index = linear_search(arr, x)
    if index != -1:
        return index
    else:
        return "Element not found"

print(exists_in_list_and_index(numbers, 7)) # Output: 3
print(exists_in_list_and_index(numbers, 2)) # Output: Element not found