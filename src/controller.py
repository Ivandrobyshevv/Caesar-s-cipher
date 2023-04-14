from typing import Union

from src.exceptions import check_language, check_operation, check_shift, check_text


def get_alfabet_or_none() -> Union[str, None]:
    language_value = input("Выберите алфавит\n1-Русский\n2-Английский\n>> ")
    alfabet = check_language(language_value)
    return alfabet


def get_text_or_none(alfabet: str) -> Union[str, None]:
    text_value = input("Входной текст\n>> ")
    if check_text(text_value, alfabet):
        return text_value
    print("Не корректный текст!")


def get_operation_or_none() -> Union[bool, None]:
    operation_value = input("Операция\n1-Зашифровать\n2-Расшифровать\n>> ")
    operation = check_operation(operation_value)
    return operation


def get_shift_or_none(alphabet: str) -> Union[int, None]:
    alphabet_length = len(alphabet)
    shift_value = input(f"Сдвиг (от 1 до {alphabet_length - 1} ): ")
    shift = check_shift(alphabet_length, shift_value)
    return shift
