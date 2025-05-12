def display_vowel_report(message, required_case):
    """
    Displays whether the number of vowels in the message is odd or even,
    depending on the required_case parameter.
    """
    count = get_vowel_count(message, required_case)
    case = required_case.lower()
    descriptor = (
        "vowels" if case == "both"
        else "lower case vowels" if case == "lower"
        else "upper case vowels"
    )
    parity = "odd" if is_odd(count) else "even"
    print(f"There is an {parity} number of {descriptor} in the message.")