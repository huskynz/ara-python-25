# 1-1-1
# Peter
# peter@husky.nz
# wow


def get_vowel_count(message: str, required_case="") -> int:
    """
    Vowel Count
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    message = message.replace("#","").replace(".","").strip()
    
    count = sum(1 for ch in message if ch in vowels)
    return count

print(get_vowel_count('The function does not display any output therefore NO strings are given.', 'lower'))
