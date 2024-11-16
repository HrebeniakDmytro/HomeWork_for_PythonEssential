class TrainerNotFoundError(Exception):
    pass

sports_types = {
    1: "Футбол",
    2: "Баскетбол",
    3: "Плавання",
    4: "Теніс",
    5: "Йога"
}

trainers = {
    "Іваненко": "Футбол",
    "Петренко": "Баскетбол",
    "Сидоренко": "Плавання",
    "Коваленко": "Теніс",
    "Олійник": "Йога"
}

schedule = {
    "Футбол": "Пн, Ср, Пт - 18:00",
    "Баскетбол": "Вт, Чт - 17:30",
    "Плавання": "Пн, Ср, Пт - 19:00",
    "Теніс": "Вт, Чт - 18:30",
    "Йога": "Сб, Нд - 10:00"
}

training_cost = {
    "Футбол": 300,
    "Баскетбол": 350,
    "Плавання": 400,
    "Теніс": 450,
    "Йога": 250
}

def display_sports():
    print("\nПерелік видів спорту:")
    for key, sport in sports_types.items():
        print(f"{key}. {sport}")

def display_trainers():
    print("\nКоманда тренерів:")
    for surname, sport in trainers.items():
        print(f"Тренер: {surname}, Вид спорту: {sport}")

def display_schedule():
    print("\nРозклад тренувань:")
    for sport, time in schedule.items():
        print(f"{sport}: {time}")

def display_training_cost():
    print("\nВартість тренувань:")
    for sport, cost in training_cost.items():
        print(f"{sport}: {cost} грн")

def search_trainer_by_surname():
    try:
        surname = input("\nВведіть прізвище тренера для пошуку: ")
        if surname not in trainers:
            raise TrainerNotFoundError(f"Тренера з прізвищем '{surname}' не знайдено.")
        print(f"Тренер: {surname}, Вид спорту: {trainers[surname]}")
    except TrainerNotFoundError as e:
        print(f"Помилка: {e}")

def main():
    while True:
        print("\nМеню спортивного комплексу:")
        print("1 - Перелік видів спорту")
        print("2 - Команда тренерів")
        print("3 - Розклад тренувань")
        print("4 - Вартість тренування")
        print("5 - Пошук тренера за прізвищем")
        print("0 - Вихід")
        
        choice = input("\nВиберіть пункт меню (0-5): ").strip()

        if choice == "1":
            display_sports()
        elif choice == "2":
            display_trainers()
        elif choice == "3":
            display_schedule()
        elif choice == "4":
            display_training_cost()
        elif choice == "5":
            search_trainer_by_surname()
        elif choice == "0":
            print("Програма завершена.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

main()
