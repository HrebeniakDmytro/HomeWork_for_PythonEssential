def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Помилка: Ділення на нуль неможливе.")
    return a / b

def power(a, b):
    if a == 0 and b < 0:
        raise ValueError("Помилка: Нуль не можна зводити в негативний степінь.")
    return a ** b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введіть коректне число.")

def calculator():
    print("Простий калькулятор підтримує операції: +, -, *, /, ^ (піднесення до степеня).")
    
    while True:
        num1 = get_number("Введіть перше число: ")
        operation = input("Введіть операцію (+, -, *, /, ^) або 'q' для виходу: ")
        
        if operation.lower() == 'q':
            print("Програма завершена.")
            break
        
        num2 = get_number("Введіть друге число: ")
        
        try:
            if operation == '+':
                result = add(num1, num2)
            elif operation == '-':
                result = subtract(num1, num2)
            elif operation == '*':
                result = multiply(num1, num2)
            elif operation == '/':
                result = divide(num1, num2)
            elif operation == '^':
                result = power(num1, num2)
            else:
                print("Помилка: Невідома операція.")
                continue
            
            print(f"Результат: {result}")
        except ValueError as e:
            print(e)


calculator()
