from functions import reverse_string, count_vowels, is_palindrome


def test_reverse_string():
    """
    Проверяет корректность работы функции reverse_string,
    с различными строками, включая пустые строки и строки с пробелами.
    """
    # Тестирование пустой строки
    assert reverse_string("") == ""
    # Тестирование строки с одним символом
    assert reverse_string("a") == "a"
    # Тестирование строки с пробелами
    assert reverse_string("summer sea") == "aes remmus"
    # Тестирование нормальной строки
    assert reverse_string("summer") == "remmus"


def test_count_vowels():
    """
    Проверяет подсчёт гласных в строках функции count_vowels,
    с различными символами и регистрами.
    """
    # Тестирование пустой строки
    assert count_vowels("") == 0
    # Тестирование строки без гласных
    assert count_vowels("bcdfgh") == 0
    # Тестирование строки с гласными
    assert count_vowels("aeiou") == 5
    # Тестирование строки с различными регистрами
    assert count_vowels("AEIOUaeiou") == 10
    # Тестирование строки со смешанными символами
    assert count_vowels("sUmmEr SeA") == 4


def test_is_palindrome():
    """
    Проверяет, что функция is_palindrome,
    корректно определяет палиндромы и непалиндромы.
    """
    # Тестирование пустой строки
    assert is_palindrome("") == True
    # Тестирование палиндрома с одним символом
    assert is_palindrome("a") == True
    # Тестирование истинного палиндрома
    assert is_palindrome("radar") == True
    # Тестирование строки не являющейся палиндромом
    assert is_palindrome("summer") == False
    # Тестирование палиндрома с пробелами
    assert is_palindrome("no lemon, no melon") == True
