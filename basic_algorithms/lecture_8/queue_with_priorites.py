# Черга з пріоритетами - це абстрактна структура даних, яка дозволяє 
# додавати елементи в довільному порядку, але видаляти їх у за пріоритетом,
# а не як в звичайній черзі - за принципом "перший прийшов - перший вийшов".

# черги з пріоритетами використовуються в алгоритмах, системах обробки, планувальниках завдань
# Один із способів реалізації черги з пріоритетами - за допомогою купи (heap)

# 1. Вставка (enqueue) - додаємо завдання в чергу з пріоритетами
# 2. Видалення (dequeue) - коли система готова обробити наступне завдання, 
# вона дивиться на завдання з найвищим пріоритетом (або найнижчим, залежно від того,
# як визначено пріоритет) і видаляє його з черги для обробки
# 3. Обробка - після видалення завдання з черги його можна обробити: виконати функцію,
# відправити повідомлення тощо

# Імітація черги з пріоритетами для конвертації зображень
def convert_image(file_name, target_format):
    # Припустимо, що ця функція конвертує зображення (тут просто імітація)
    print(f"Конвертація {file_name} до {target_format} формату...")
    return f"{file_name.split('.')[0]}.{target_format}"

# Реалізація самої черги з пріоритетом

import heapq  # Імпортуємо модуль heapq для роботи з чергою з пріоритетом

class PriorityQueue:
    def __init__(self):  # Конструктор класу
        self.queue = []  # Ініціалізуємо порожній список для зберігання елементів черги

    def enqueue(self, task, priority):  # Метод для додавання елемента до черги
        heapq.heappush(self.queue, (-priority, task))  # Додаємо елемент до черги з оберненим пріоритетом (щоб найвищий пріоритет мав найменше значення)

    def dequeue(self):  # Метод для вилучення елемента з черги
        return heapq.heappop(self.queue)[1]  # Вилучаємо елемент з найвищим пріоритетом та повертаємо тільки завдання

    def is_empty(self):  # Метод для перевірки, чи порожня черга
        return not bool(self.queue)  # Повертаємо True, якщо черга порожня, і False, якщо ні

def main():
    pq = PriorityQueue()

    # Користувачі завантажують свої зображення
    pq.enqueue(("sample1.jpg", "png"), 1)  # Основний користувач
    pq.enqueue(("premium_sample.jpg", "bmp"), 10)  # Преміум-користувач
    pq.enqueue(("sample2.jpg", "tiff"), 1)  # Основний користувач

    while not pq.is_empty():
        file_name, target_format = pq.dequeue()
        output_file = convert_image(file_name, target_format)
        print(f"Зображення було успішно конвертовано і збережено як {output_file}!")

if __name__ == "__main__":
    main()