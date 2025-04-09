# 1-1-1
# Peter
# peter@husky.nz
# wow


def get_number_as_string(message, min_length):
    """
    THis works somehow, my code works somewhat
    """
    UserPinNum = input(message).strip()

    UserPinNumCheck = UserPinNum.isnumeric()

    if UserPinNumCheck == True:
        print("Yes")

    elif UserPinNumCheck == False:
        print("Digits only please.")


# Test parameter names
pin_message = 'Please enter your pin number: '
min_digits = 4
entered_number = get_number_as_string(message = pin_message, min_length = min_digits)
print(f'The number is {entered_number}')

