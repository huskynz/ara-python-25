# 1-1-1
# Peter
# peter@husky.nz
# wow

def is_punctuated_correctly(sentence: str) -> bool:
    """
    Checks if the given string ends with a full stop, exclamation mark, or question mark,
    ignoring any trailing spaces.
    """
    return sentence.rstrip()[-1] in ".!?" if sentence.strip() else False