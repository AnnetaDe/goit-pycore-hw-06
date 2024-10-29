from errors import input_error
from helper_errors_classes import ArgsNotEnought, CustomKeyError,  CustomAlreadyExistsError


def normalize_input(user_input):
    return user_input.strip().lower()


@input_error
def parse_input(user_input):
    if not user_input:
        return None, None
    if " " not in user_input:
        return normalize_input(user_input), None

    cmd, *args = user_input.split()
    cmd = normalize_input(cmd)

    return cmd, *args


@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ArgsNotEnought(args)
    name, phone = args
    if name in contacts:
        raise CustomAlreadyExistsError(name)

    contacts[name] = phone
    return f"Contact added {name} - {phone}."


def all_contacts(contacts):

    for name, phone in contacts.items():
        yield (f'{name} - {phone}')


@input_error
def change_username_phone(args, contacts):
    print('args', args)
    if len(args) != 2:
        raise ArgsNotEnought(args)
    if args[0] not in contacts:
        raise CustomKeyError(args[0])
    name, phone = args
    contacts[name] = phone if name in contacts else None
    return f"Contact changed, new contact is: {name} - {phone}."


@input_error
def phone_by_name(args, contacts):
    print('args', args)
    name = args[0]
    if name not in contacts:
        raise CustomKeyError(name)

    return contacts.get(name, "Contact not found.")


def execute_command(command, args, contacts):
    if command in ["close", "exit"]:
        print("Good bye!")
        return
    elif command == "hello":
        print("How can I help you?")
    elif command == "add":
        print(add_contact(args, contacts))
    elif command == "all":
        for contact in all_contacts(contacts):
            print(contact)
    elif command == "change":
        print(change_username_phone(args, contacts))
    elif command == "phone":
        print(phone_by_name(args, contacts))
    elif command == "phone":
        print(phone_by_name(args, contacts))
    elif command == "help":
        print("Commands: hello, add, all, change, phone, close, exit, help")
