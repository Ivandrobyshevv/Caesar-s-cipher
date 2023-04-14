from src.db import ALFABET
from src.exceptions import check_language, check_operation, check_shift, check_text


def test_check_language():
    assert check_language("1") == ALFABET.get(1)
    assert check_language("2") == ALFABET.get(2)
    assert check_language("3") is None
    assert check_language("a") is None


def test_check_operation():
    assert check_operation("1") == True
    assert check_operation("2") == False
    assert check_operation("3") is None
    assert check_operation("a") is None
    assert check_operation(" ") is None


def test_check_shift_ru():
    length_alfabet = 33
    assert check_shift(length_alfabet, "1") == 1
    assert check_shift(length_alfabet, "32") == 32
    assert check_shift(length_alfabet, "0") is None
    assert check_shift(length_alfabet, "33") is None
    assert check_shift(length_alfabet, "35") is None


def test_check_shift_eng():
    length_alfabet = 26
    assert check_shift(length_alfabet, "1") == 1
    assert check_shift(length_alfabet, "25") == 25
    assert check_shift(length_alfabet, "0") is None
    assert check_shift(length_alfabet, "26") is None
    assert check_shift(length_alfabet, "27") is None


def test_check_text_ru():
    alfabet = ALFABET.get(1)
    assert check_text("абвлвфф вфвфвф", alfabet) == True
    assert check_text("абвлвфф, вфвфвф", alfabet) == True
    assert check_text('ldalsdla', alfabet) == False


def test_check_text_eng():
    alfabet = ALFABET.get(2)
    assert check_text("aalldaa ldaslds", alfabet) == True
    assert check_text("AAAAAAA, slkaskdsa", alfabet) == True
    assert check_text('выдвыдфвдф', alfabet) == False
