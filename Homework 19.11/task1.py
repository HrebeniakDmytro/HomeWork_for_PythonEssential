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

print(contact1.get_contact())
print(contact1.sent_message("Hello, John!"))

print(update_contact1.get_message())

print("\nАтрибути об'єкта contact1 (Contact):")
print(contact1.__dict__)  

print("\nАтрибути об'єкта update_contact1 (UpdateContact):")
print(update_contact1.__dict__)  

print("\nБатьківський клас класу UpdateContact:")
print(UpdateContact.__base__)  

print("\nБатьківські класи класу UpdateContact:")
print(UpdateContact.__bases__)  
