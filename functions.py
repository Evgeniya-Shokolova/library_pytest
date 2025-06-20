def reverse_string(s: str) -> str:
    """Принимает строку и возвращает её перевёрнутую версию."""
    return s[::-1]


def count_vowels(s: str) -> int:
    """Принимает строку и возвращает количество гласных в ней."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


def is_palindrome(s: str) -> bool:
    """Принимает строку и возвращает True, если строка является палиндромом."""
    # Преобразуем строку в нижний регистр и убираем пробелы для корректной проверки палиндрома
    normalized_str = ''.join(filter(str.isalnum, s)).lower()
    return normalized_str == normalized_str[::-1]
