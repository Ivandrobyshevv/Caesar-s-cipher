from src.controller import get_alfabet, get_operation, get_text, get_shift
from src.caesar import Caesar


def start():
    result = None
    while True:
        alfabet = get_alfabet()
        if alfabet is None:
            continue
        caesar = Caesar(alfabet)
        text = get_text()
        operator = get_operation()
        if operator is None:
            continue
        shift = get_shift(alfabet)
        if shift is None:
            continue
        if operator:
            result = caesar.encryption_caesar(text=text, shift=shift)
        else:
            result = caesar.decryption_caesar(text=text, shift=shift)
        print(result)


if __name__ == '__main__':
    start()
