# 1-1-1
# Peter
# peter@husky.nz
# wow


def get_number_as_string(message, min_length):
    """
    THis works somehow, my code works somewhat
    """
    while True:
        user_input = input(message).replace(" ","")

        if not user_input.isdigit():
          print("Digits only please.")
        elif len(user_input) < min_length:
           print(f"The number must be at least {min_length} digits long.")
        else:
           return user_input  





# Test parameter names
pin_message = 'Please enter your pin number: '
min_digits = 4
entered_number = get_number_as_string(message = pin_message, min_length = min_digits)
print(f'The number is {entered_number}')