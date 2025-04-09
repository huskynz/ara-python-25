# 1-1-1
# Peter
# peter@husky.nz
# wow


def welcome_student(first_name: str, greeting_phrase: str = 'Kia ora') -> str:
    """
    Returns a welcome message for a student using the given first name and greeting phrase.
    """
    return f"{greeting_phrase} {first_name}."