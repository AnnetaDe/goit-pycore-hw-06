# Розробіть систему для управління адресною книгою.


# Сутності:

# Field: Базовий клас для полів запису.
# Name: Клас для зберігання імені контакту. Обов'язкове поле.
# Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
# Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
# AddressBook: Клас для зберігання та управління записами.


# Функціональність:

# AddressBook:Додавання записів.
# Пошук записів за іменем.
# Видалення записів за іменем.
# Record:Додавання телефонів.
# Видалення телефонів.
# Редагування телефонів.
# Пошук телефону.
import re


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class Phone(Field):
    def __init__(self, value):
        self.value = value
        if len(value) != 10:
            raise ValueError('Phone number must be 10 digits')

    def __str__(self):
        return self.value


class Record:
    def __init__(self, name, phones=None):
        self.name = name
        self.phones = phones if phones else []

    def add_phone(self, phone):
        self.phones.append(phone)
        return self.phones

    def __str__(self):
        return f'{self.name} - {", ".join(phone.value for phone in self.phones)}'

    @staticmethod
    def is_valid_phone(phone_number):
        pattern = r"^\+?[0-9\s\-\(\)]+$"
        return bool(re.match(pattern, phone_number)) and len(phone_number) >= 10


class AddressBook:
    def __init__(self):
        self.records = set()

    def add_record(self, record):
        self.records.add(record)

    def prompt_add_new_record(self, name):
        user_input = input(
            f"Do you want to add a new record for {name}? (y/n): ")
        if user_input.lower() == 'y':
            new_record = Record(Name(name))
            while True:
                new_phone = input(
                    f"Provide a phone number for {new_record.name.value} or press Enter to skip: ")
                if new_phone == "":
                    print("No phone number added, but you can add it later.\n")
                    break

                elif Record.is_valid_phone(new_phone):
                    new_record.add_phone(Phone(new_phone))
                    print(f"Phone number added: {new_phone}")
                    break
                else:
                    print("No phone number added, but you can add it later.\n")
            self.add_record(new_record)
            print(f"Record added: {new_record}")
            return new_record, self.records
        elif user_input.lower() == 'n':
            return "Okay. Let me know if you need further assistance."

    def prompt_add_new_phone(self, record):
        user_input = input(
            f"Add new phone number to {record.name.value}? (y/n): ")
        if user_input.lower() == 'y':
            phone = Phone(input("Enter phone number: "))
            record.add_phone(phone)
            print(f"Updated record: {record}")
            return record

    def prompt_action(self, record):
        if record:
            action = input(
                f"{record.name.value} found. What do you want to do? "
                "(add phone, delete record, exit,change phone) (a/d/e/c): "
            )
            if action == 'a':
                return self.prompt_add_new_phone(record)
            elif action == 'd':
                return self.delete_record(record.name.value)
            elif action == 'c':
                return self.change_phone(record, Phone(input("Enter old phone number: ")))

            elif action == 'e':
                return "Okay. Let me know if you need further assistance."

    def find_record(self, name):
        for record in self.records:
            if record.name.value == name:
                print(f"Found record: {record}")
                return record, self.prompt_action(record)
        return self.prompt_add_new_record(name)

    def delete_record(self, name):
        record = self.find_record(name)
        if record:
            self.records.remove(record)
            print(f"Record deleted for {name}")
        return record

    def find_record_by_phone(self, phone):
        for record in self.records:
            if phone in record.phones:
                print(f"Found record: {record}")
                return record

    def change_phone(self, record, old_phone):
        try:
            record.phones.remove(old_phone)
        except ValueError:
            print(
                f"The phone number {old_phone.value} does not exist in the record.")
            return record

        while True:
            new_phone_input = input("Enter new phone number: ")
            if new_phone_input == "":
                print("No new phone number provided. Operation cancelled.")
                return record

            if Record.is_valid_phone(new_phone_input):
                new_phone = Phone(new_phone_input)
                record.add_phone(new_phone)
                print(f"Updated record: {record}")
                return record
            else:
                print("Invalid phone number. Please try again.")

    def __str__(self):
        if not self.records:
            return "No records found."
        return '\n'.join(str(record) for record in self.records)


my_address_book = AddressBook()

record1 = Record(Name('John'), [Phone('1234567890')])
record2 = Record(Name('Ann'), [Phone('1234567890')])
record3 = Record(Name('Johny'), [Phone('1234567895')])
# print(my_address_book.find_record(Name('John')))
# print(my_address_book.find_record(Name('Ann')))

record1.add_phone(Phone('1111111111'))
record1.add_phone(Phone('1111111112'))
record1.add_phone(Phone('1111111113'))
record2.add_phone(Phone('1111111114'))
record2.add_phone(Phone('1111111115'))
record2.add_phone(Phone('1111111116'))
record3.add_phone(Phone('1111111117'))
record3.add_phone(Phone('1111111118'))
record3.add_phone(Phone('1111111119'))
# print(record1, record2)
my_address_book.add_record(record1)
my_address_book.add_record(record2)
my_address_book.add_record(record3)
my_address_book.find_record('John')

my_address_book.find_record(name='Johnatan')
my_address_book.find_record_by_phone('1111111111')
print("adress_book", my_address_book, sep='\n')
