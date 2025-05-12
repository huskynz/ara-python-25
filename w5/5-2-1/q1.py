# 1-1-1
# Peter
# peter@husky.nz
# wow

def get_vowel_count(message, required_case='both'):
    """
    Vowel Count
    """ 
    required_case = required_case.lower()
    if required_case not in ['both', 'lower', 'upper']:
        required_case = 'both'

    vowels_lower = 'aeiou'
    vowels_upper = 'AEIOU'

    if required_case == 'lower':
        vowels = vowels_lower
    elif required_case == 'upper':
        vowels = vowels_upper
    else:
        vowels = vowels_lower + vowels_upper

    count = sum(1 for char in message if char in vowels)
    return count