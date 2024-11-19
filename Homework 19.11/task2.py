class Contact:
    def __init__(self, surname, name, age, mob_phone, email):
        self.surname = surname
        self.name = name
        self.age = age
        self.mob_phone = mob_phone
        self.email = email

    def get_contact(self):
        return f"Contact Info: {self.surname} {self.name}, Age: {self.age}, Phone: {self.mob_phone}, Email: {self.email}"
    
    def sent_message(self, message):
        return f"Sending message: '{message}' to {self.name} at {self.mob_phone}"

class UpdateContact(Contact):
    def __init__(self, surname, name, age, mob_phone, email, job):
        super().__init__(surname, name, age, mob_phone, email)
        self.job = job

    def get_message(self):
        return f"Updated Contact Info: {self.surname} {self.name}, Age: {self.age}, Phone: {self.mob_phone}, Email: {self.email}, Job: {self.job}"

contact1 = Contact("Smith", "John", 30, "+123456789", "john.smith@example.com")
update_contact1 = UpdateContact("Doe", "Jane", 28, "+987654321", "jane.doe@example.com", "Software Engineer")

attributes = ['surname', 'name', 'age', 'mob_phone', 'email', 'job']

print("Операції з об'єктом contact1 (Contact)")
for attr in attributes:
    if hasattr(contact1, attr):
        print(f"У об'єкта contact1 є атрибут '{attr}'. Його значення: {getattr(contact1, attr)}")
    else:
        print(f"У об'єкта contact1 немає атрибуту '{attr}'. Додаємо його за допомогою setattr().")
        setattr(contact1, attr, "Default Value")
        print(f"Додано атрибут '{attr}' з значенням: {getattr(contact1, attr)}")

    setattr(contact1, attr, "Updated Value")
    print(f"Атрибут '{attr}' оновлено. Його нове значення: {getattr(contact1, attr)}")

    if hasattr(contact1, attr):
        delattr(contact1, attr)
        print(f"Атрибут '{attr}' видалено.")
    else:
        print(f"Неможливо видалити атрибут '{attr}', оскільки він не існує.")

print("\nОперації з об'єктом update_contact1 (UpdateContact)")
for attr in attributes:
    if hasattr(update_contact1, attr):
        print(f"У об'єкта update_contact1 є атрибут '{attr}'. Його значення: {getattr(update_contact1, attr)}")
    else:
        print(f"У об'єкта update_contact1 немає атрибуту '{attr}'. Додаємо його за допомогою setattr().")
        setattr(update_contact1, attr, "Default Value")
        print(f"Додано атрибут '{attr}' з значенням: {getattr(update_contact1, attr)}")

    setattr(update_contact1, attr, "Updated Value")
    print(f"Атрибут '{attr}' оновлено. Його нове значення: {getattr(update_contact1, attr)}")

    if hasattr(update_contact1, attr):
        delattr(update_contact1, attr)
        print(f"Атрибут '{attr}' видалено.")
    else:
        print(f"Неможливо видалити атрибут '{attr}', оскільки він не існує.")
