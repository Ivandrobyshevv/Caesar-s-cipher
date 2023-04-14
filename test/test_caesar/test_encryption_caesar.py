from src.caesar import Caesar
from src.db import ALFABET


def test_encryption_caesar_ru():
    test_caesar = Caesar(alfabet=ALFABET.get(1))
    assert test_caesar.encryption_caesar("Иван", 1) == "Йгбо"
    assert test_caesar.encryption_caesar("Иван1", 32) == "Збям1"
    assert test_caesar.encryption_caesar("Иван, привет!", 32) == "Збям, опзбдс!"


def test_encryption_caesar_eng():
    test_caesar = Caesar(alfabet=ALFABET.get(2))
    assert test_caesar.encryption_caesar("Ivan", 1) == "Jwbo"
    assert test_caesar.encryption_caesar("Ivan1", 5) == "Nafs1"
    assert test_caesar.encryption_caesar("Ivan, hi!", 25) == "Huzm, gh!"
