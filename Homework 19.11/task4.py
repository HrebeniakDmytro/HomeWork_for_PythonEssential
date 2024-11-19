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
contact2 = Contact("Brown", "Alice", 35, "+234567890", "alice.brown@example.com")

update_contact1 = UpdateContact("Doe", "Jane", 28, "+987654321", "jane.doe@example.com", "Software Engineer")
update_contact2 = UpdateContact("White", "Tom", 40, "+876543210", "tom.white@example.com", "Project Manager")

def print_info():
    print("Інформація про клас Contact та його екземпляри")
    print(f"Клас Contact (__dict__): {Contact.__dict__}")
    print(f"Екземпляр contact1 (__dict__): {contact1.__dict__}")
    print(f"Екземпляр contact2 (__dict__): {contact2.__dict__}")

    print("\nІнформація про клас UpdateContact та його екземпляри")
    print(f"Клас UpdateContact (__dict__): {UpdateContact.__dict__}")
    print(f"Екземпляр update_contact1 (__dict__): {update_contact1.__dict__}")
    print(f"Екземпляр update_contact2 (__dict__): {update_contact2.__dict__}")

print("Початкова інформація")
print_info()

print("\nВидалення атрибуту job з екземплярів класу UpdateContact")
if hasattr(update_contact1, 'job'):
    delattr(update_contact1, 'job')
    print("Атрибут 'job' видалено з update_contact1.")
if hasattr(update_contact2, 'job'):
    delattr(update_contact2, 'job')
    print("Атрибут 'job' видалено з update_contact2.")

print("\nІнформація після видалення атрибуту job")
print_info()
