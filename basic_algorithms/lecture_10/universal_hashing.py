# Універсальне хешування — це метод, при якому вибирається хеш-функція випадковим чином
# із сімейства хеш-функцій, що гарантує, що для будь-якого набору ключів імовірність
# колізій буде мінімальною.

# Основна ідея універсального хешування полягає в тому, щоб мати безліч можливих хеш-функцій
# та випадково вибирати одну з них. Це допомагає знизити ймовірність "поганих" випадків, 
# коли багато ключів потрапляють у ту саму позицію в хеш-таблиці.

import random  # Імпортуємо модуль random для генерації випадкових чисел


class UniversalHash:
    def __init__(self, m, max_key):
        # m - розмір хеш-таблиці
        # max_key - максимальне значення ключа
        self.m = m  # Зберігаємо розмір хеш-таблиці
        self.p = self._next_prime(max_key)  # Знаходимо просте число, більше max_key
        self.a = random.randint(1, self.p - 1)  # Випадкове число a у діапазоні [1, p-1]
        self.b = random.randint(0, self.p - 1)  # Випадкове число b у діапазоні [0, p-1]

    def _next_prime(self, n):
        # Знаходимо наступне просте число більше n
        while True:
            n += 1  # Збільшуємо n на 1
            for i in range(2, int(n ** 0.5) + 1):  # Перевіряємо чи n є простим числом
                if n % i == 0:  # Якщо n ділиться на i, то це не просте число
                    break
            else:
                return n  # Якщо n не ділиться на жодне число, то воно є простим

    def hash(self, key):
        # Хешування ключа key за допомогою універсальної хеш-функції
        return ((self.a * key + self.b) % self.p) % self.m  # Обчислюємо хеш-значення

# Приклад використання:
hasher = UniversalHash(100, 1000)  # Створюємо об'єкт хешування з розміром таблиці 100 і максимальним ключем 1000
print(hasher.hash(123))  # Хешуємо ключ 123 і виводимо результат
print(hasher.hash(456))  # Хешуємо ключ 456 і виводимо результат
