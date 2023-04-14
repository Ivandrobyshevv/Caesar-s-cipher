from src.controller import get_text_or_none, get_alfabet_or_none, \
    get_operation_or_none, get_shift_or_none
from src.caesar import Caesar


def get_caesar_result(operator: bool, caesar: Caesar, text: str, shift: int) -> str:
    if operator:
        return caesar.encryption_caesar(text, shift)
    return caesar.decryption_caesar(text=text, shift=shift)


def show_result(text: str, result: str) -> None:
    print('-' * 20)
    print(f'Входной текст: {text}\nРезультат: {result}')
    print('-' * 20)
    print()


def start():
    while True:
        alfabet = get_alfabet_or_none()
        if alfabet is None:
            continue
        caesar = Caesar(alfabet)
        text = get_text_or_none(alfabet)
        if text is None:
            continue
        operator = get_operation_or_none()
        if operator is None:
            continue
        shift = get_shift_or_none(alfabet)
        if shift is None:
            continue
        caesar_result = get_caesar_result(operator, caesar, text, shift)
        show_result(text, caesar_result)
        repeat = input("Повторить операцию [y/n]?: ")
        if repeat.lower() in ('no', 'n', 'н', 'нет'):
            print("До свидания!")
            break
        if repeat.lower() not in ('y', 'yes', 'д', 'да'):
            print(f"Не известное значение - {repeat}")
            break


if __name__ == '__main__':
    start()
