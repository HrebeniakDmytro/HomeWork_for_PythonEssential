class Employee:
    def __init__(self, first_name, last_name, department, start_year):
        if not first_name or not last_name or not department:
            raise ValueError("Помилка: Ім'я, прізвище та відділ не можуть бути порожніми.")
        
        if not isinstance(start_year, int) or start_year < 1900 or start_year > 2024:
            raise ValueError("Помилка: Рік початку роботи має бути коректним числом у межах 1900-2024.")
        
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.start_year = start_year

    def __str__(self):
        return f"{self.first_name} {self.last_name}, Відділ: {self.department}, Рік початку роботи: {self.start_year}"

def get_employee_data():
    while True:
        try:
            first_name = input("Введіть ім'я співробітника: ")
            if not first_name:  
                return None  
            
            last_name = input("Введіть прізвище співробітника: ")
            department = input("Введіть відділ співробітника: ")
            start_year = int(input("Введіть рік початку роботи: "))

            return Employee(first_name, last_name, department, start_year)
        except ValueError as e:
            print(e)
            print("Спробуйте ще раз.")

def filter_employees_by_year(employees, year):
    filtered_employees = []
    for employee in employees:
        if employee.start_year > year:
            filtered_employees.append(employee)
    return filtered_employees

def main():
    employees = []

    print("Введіть список співробітників. Для завершення введення натисніть Enter без введення імені.")
    while True:
        employee = get_employee_data()
        if employee is None:  
            print("Введення завершено.")
            break
        employees.append(employee)

    try:
        filter_year = int(input("Введіть рік для фільтрації співробітників (показати тих, хто прийнятий після цього року): "))
    except ValueError:
        print("Помилка: рік має бути числом.")
        return

    filtered_employees = filter_employees_by_year(employees, filter_year)
    if filtered_employees:
        print("\nСпівробітники, які були прийняті після року", filter_year)
        for emp in filtered_employees:
            print(emp)
    else:
        print("Немає співробітників, які були прийняті після вказаного року.")

main()
