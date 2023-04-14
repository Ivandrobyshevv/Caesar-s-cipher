import re
from typing import Union

from src.db import ALFABET, OPERATIONS

ERROR_MASSAGE = "Вы ввели не число!"


def check_language(language: str) -> Union[str, None]:
    if language.isdigit():
        try:
            alfabet = ALFABET.get(int(language))
            return alfabet
        except KeyError:
            print(f"Не корректное значение, вы ввели {language}!")
    else:
        print(ERROR_MASSAGE)


def check_operation(operation_value: str) -> Union[bool, None]:
    if operation_value.isdigit():
        try:
            operation = OPERATIONS.get(int(operation_value))
            return operation
        except KeyError:
            print(f"Не корректное значение, вы ввели {operation_value}!")
    else:
        print(ERROR_MASSAGE)


def check_text(text: str, alphabet: str) -> bool:
    return bool(set(alphabet).intersection(set(text.upper())))


def check_shift(length_alfabet: int, shift_value: str) -> Union[int, None]:
    if shift_value.isdigit():
        try:
            shift = int(shift_value)
            if shift > length_alfabet-1 or shift < 1:
                print(f"Не корректное значение, вы ввели {shift_value}!")
                return
            return shift
        except ValueError:
            print(f"Не корректное значение, вы ввели {shift_value}!")
    else:
        print(ERROR_MASSAGE)
