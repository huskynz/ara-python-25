# 1-1-1
# Peter
# peter@husky.nz
# wow


def get_number_as_string(message, min_length):
    """
    THis works somehow, my code works somewhat
    """
    UserPinNum = input(message).strip().replace(" ", "")

    UserPinNumCheck = UserPinNum.isnumeric()

    if UserPinNumCheck == True:
        UserPinNum = int(UserPinNum)
        UserPinNumlen = len(str(UserPinNum))
        UserPinVaild = False

        if UserPinNumlen < min_length:
            print(f"The number must be at least {min_length} digits long.")
        
        else:
            return(str(UserPinNum))
    
    else:
        while UserPinVaild == False:
           if UserPinNumCheck == False:
            print("Digits only please.")
            UserPinVaild = False
           elif UserPinNumCheck == True:
            UserPinVaild = True 
            get_number_as_string(message, min_length)






# Test parameter names
pin_message = 'Please enter your pin number: '
min_digits = 4
entered_number = get_number_as_string(message = pin_message, min_length = min_digits)
print(f'The number is {entered_number}')