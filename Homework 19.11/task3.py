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

print("Перевірка екземплярів класів за допомогою isinstance()")
print(f"contact1 є екземпляром класу Contact: {isinstance(contact1, Contact)}")
print(f"contact1 є екземпляром класу UpdateContact: {isinstance(contact1, UpdateContact)}")
print(f"update_contact1 є екземпляром класу UpdateContact: {isinstance(update_contact1, UpdateContact)}")
print(f"update_contact1 є екземпляром класу Contact: {isinstance(update_contact1, Contact)}")
print(f"contact2 є екземпляром класу Contact: {isinstance(contact2, Contact)}")
print(f"update_contact2 є екземпляром класу Contact: {isinstance(update_contact2, Contact)}")

print("\nПеревірка класів-нащадків за допомогою issubclass()")
print(f"UpdateContact є підкласом Contact: {issubclass(UpdateContact, Contact)}")
print(f"Contact є підкласом UpdateContact: {issubclass(Contact, UpdateContact)}")
print(f"Contact є підкласом Contact: {issubclass(Contact, Contact)}")
print(f"UpdateContact є підкласом UpdateContact: {issubclass(UpdateContact, UpdateContact)}")
