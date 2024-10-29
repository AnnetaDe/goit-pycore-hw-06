

from helper_errors_classes import CommandValidator
from commands import execute_command, parse_input


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        try:
            validator = CommandValidator(command, args)
            validator.validate()
            execute_command(command, args, contacts)
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
