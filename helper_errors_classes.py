class CustomException(Exception):
    pass


class CustomAttributeError(CustomException):
    def __init__(self, name, obj):
        self.name = name
        self.obj = obj
        message = f'the name "{name}" is not found in "{obj}".'
        super().__init__(message)


class CustomAlreadyExistsError(CustomException):
    def __init__(self, name):
        self.name = name
        message = f'Contact "{
            name}" already exists. if you want to change it, use "change"'
        super().__init__(message)


class ArgsNotEnought(CustomException):
    def __init__(self, args):
        message = f'It should be 2 arguments, but got {len(args)}.'
        super().__init__(message)


class CustomKeyError(CustomException):
    def __init__(self, key):
        self.key = key
        message = f'Key "{
            key}" is not found in dict, would you mind to add it first? '
        super().__init__(message)


class CommandValidator:
    VALID_COMMANDS = ["hello", "add", "all",
                      "change", "phone", "close", "exit", "help"]

    def __init__(self, command, args):
        self.command = command
        self.args = args

    def validate_command(self):
        if self.command not in self.VALID_COMMANDS:
            raise ValueError(f"I dont have this command: {self.command}")

    def validate_args(self):
        if not self.args:
            raise ValueError("No arguments provided")

    def validate(self):
        self.validate_command()
        self.validate_args()
