class InvalidInputError(Exception):
    pass

def check_user_input(value):
    if value == "заборонено":
        raise InvalidInputError("Ви ввели заборонене значення!")
    else:
        print(f"Ви ввели: {value}")

def main():
    try:
        user_input = input("Введіть будь-яке значення (не використовуйте слово 'заборонено'): ").strip()
        check_user_input(user_input)
    except InvalidInputError as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    main()
