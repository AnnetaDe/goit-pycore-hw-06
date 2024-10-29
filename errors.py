

from helper_errors_classes import ArgsNotEnought, CustomAlreadyExistsError, CustomAttributeError, CustomKeyError


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except ArgsNotEnought() as e:
            return e
        except CustomAttributeError() as e:
            return e
        except CustomKeyError() as e:
            return e
        except CustomAlreadyExistsError() as e:
            return f'{e}'
        except ValueError as e:
            return e

        except Exception as e:
            return f"unexpected error {e}"

    return inner
