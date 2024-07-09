# рекурсивне обчислення чисел Фібоначчі без мемоізації має експоненційну часову складність 
# O(2 в степені n) і може бути дуже повільним для великих значень n

# рекурсивне обчислення чисел Фібоначчі з мемоізацією

def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    else:
        value = fibonacci_memo(n-1, memo) + fibonacci_memo(n-2, memo)
        memo[n] = value
        return value
print(fibonacci_memo(10))  # Виведе: 55
# memo={} - словник, який зберігає проміжні результати обчислень
# functools.lru_cache - декоратор, який дозволяє додати мемоізацію до функції
# Least Recently Used Cache (LRU Cache) - це механізм кешування, який зберігає обмежену кількість елементів
# переваги:
# декоратор автоматично управляє структурою даних, яка зберігає проміжні результати
# декоратор можливість встановлення обмеження на розмір кешу
# недолік:
# використання пам'яті, без встановлення конкретного обмеження - значні витрати системної пам'яті

from functools import lru_cache

@lru_cache(maxsize=None)  # Unbounded cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(50))

# merge sort, quick sort, binary search, tree traversal, Evclid's algorithm - recursive algorithms

