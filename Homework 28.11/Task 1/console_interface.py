from link_shortener import LinkShortener

class ConsoleInterface:
    def __init__(self):
        self.shortener = LinkShortener()

    def run(self):
        while True:
            print("\nМеню:")
            print("1. Додати нове посилання")
            print("2. Отримати початкове посилання за короткою назвою")
            print("3. Видалити посилання")
            print("4. Показати всі посилання")
            print("5. Вийти")

            choice = input("Виберіть опцію (1-5): ")

            if choice == '1':
                original_url = input("Введіть початкове посилання: ")
                short_name = input("Введіть коротку назву: ")
                print(self.shortener.add_link(original_url, short_name))

            elif choice == '2':
                short_name = input("Введіть коротку назву: ")
                print(self.shortener.get_link(short_name))

            elif choice == '3':
                short_name = input("Введіть коротку назву для видалення: ")
                print(self.shortener.delete_link(short_name))

            elif choice == '4':
                links = self.shortener.list_links()
                if links:
                    print("\nЗбережені посилання:")
                    for short, original in links.items():
                        print(f"{short} -> {original}")
                else:
                    print("Немає збережених посилань.")

            elif choice == '5':
                print("Вихід із програми.")
                break
            else:
                print("Невірний вибір, спробуйте ще раз.")
