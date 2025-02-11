# У Python граничним значенням вважається 1000 викликів функцій - stack overflow
# Факторіал натурального числа n! = 1*2*3*...*n - добуток всіх натуральних чисел від 1 до n включно.
def factorial(n):
    print("Виклик функції factorial з n = ", n)
    if n == 0: # базовий випадок
        print("Базовий випадок, n = 1, повернення 1")
        return 1
    else:
       result = n * factorial(n-1) # рекурсивний випадок
       print("Повернення результату для n = ", n, ": ", result)
       return result 

print(factorial(5)) # виведе 120


# числа Фібоначчі - послідовність чисел, де кожне число є сумою двох попередніх чисел
# F(n)=F(n-1)+F(n-2), F(0)=0, F(1)=1

def fibonacci(n):
    if n <= 1: # базовий випадок
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # рекурсивний випадок

print(fibonacci(10)) # виведе 55
