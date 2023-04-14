from typing import Union

from src.exceptions import check_language, check_operation, check_shift


def get_alfabet() -> Union[str, None]:
    language_value = input("Алфавит\n1-Русский\n2-Английский\n>> ")
    alfabet = check_language(language_value)
    return alfabet


def get_text() -> str:
    text = input("Входной текст.\n>> ")
    return text


def get_operation() -> Union[bool, None]:
    operation_value = input("Операция\n1-Зашифровать\n2-Расшифровать\n>> ")
    operation = check_operation(operation_value)
    return operation


def get_shift(alphabet: str) -> Union[int, None]:
    alphabet_length = len(alphabet)
    shift_value = input(f"Сдвиг (от 1 до {alphabet_length}): ")
    shift = check_shift(alphabet_length, shift_value)
    return shift
