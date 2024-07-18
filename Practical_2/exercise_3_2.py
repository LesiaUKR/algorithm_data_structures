Updates to keyboard shortcuts … On Thursday, August 1, 2024, Drive keyboard shortcuts will be updated to give you first-letters navigation.Learn more
hw02.py
import turtle


def koch_snowflake(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            # Рекурсія
            t.left(angle)


def main():
    screen = turtle.Screen()
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed(0)

    order = 2
    size = 300

    # Створення сніжинки Коха

    screen.mainloop()


if __name__ == "__main__":
    main()