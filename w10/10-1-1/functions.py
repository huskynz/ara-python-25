# 1-1-1
# Peter
# peter@husky.nz
# wow

def starts_with_capital(text: str):
    """
    Checks if the first character of the given string is a capital letter.
    """
    return text[0].isupper() if text else False

def is_punctuated_correctly(sentence: str) -> bool:
    """
    Checks if the given string ends with a full stop, exclamation mark, or question mark,
    ignoring any trailing spaces.
    """
    return sentence.rstrip()[-1] in ".!?" if sentence.strip() else False

def is_odd(number: int) -> bool:
    """
    Checks if the given number is odd.
    """
    return number % 2 != 0

def is_even(value: int) -> bool:
    """
    Checks if the given number is even.
    """
    return value % 2 == 0

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Converts the given temperature from Fahrenheit to Celsius, rounded to 1 decimal place.
    """
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 1)

def welcome_student(first_name: str, greeting_phrase: str = 'Kia ora') -> str:
    """
    Returns a welcome message for a student using the given first name and greeting phrase.
    """
    return f"{greeting_phrase} {first_name}."