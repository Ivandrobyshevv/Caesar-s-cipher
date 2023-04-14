from caesar import Caesar
from db import ALFABET


def test_decryption_caesar_ru():
    test_caesar = Caesar(alfabet=ALFABET.get(1))
    assert test_caesar.decryption_caesar("Кдвп", 2) == "Иван"
    assert test_caesar.decryption_caesar("Шщскны, уиу мнфи?", 9) == "Привет, как дела?"


def test_decryption_caesar_eng():
    test_caesar = Caesar(alfabet=ALFABET.get(2))
    assert test_caesar.decryption_caesar("PQ, pwe izm gwc?", 8) == "HI, how are you?"
    assert test_caesar.decryption_caesar("Vh yqxwn wdvkna: +79177647070", 9) == "My phone number: +79177647070"
