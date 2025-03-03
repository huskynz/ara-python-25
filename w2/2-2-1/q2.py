# 1-1-1
# Peter
# peter@husky.nz
# wow

ufname = input("Please enter your first name: ")

unum1 = input(f"Hi {ufname.capitalize()}, please enter the first integer: ")

unum2 = input("Thanks. Please enter the second integer: ")

unumsameequal = unum1 is unum2
unumsameequalnot = unum1 is not unum2

unumsameelesssame = unum1 < unum2
unumsameegreater = unum1 > unum2

unumsameelesseq = unum1 <= unum2
unumsameegreatereq = unum1 >= unum2

print(" ")

print(f"It is {str(unumsameequal).lower()} that {unum1} is equal to {unum2}.")
print(f"It is {str(unumsameequalnot).lower()} that {unum1} is not equal to {unum2}.")

print(" ")

print(f"It is {str(unumsameequal).lower()} that {unum1} is less than {unum2}.")
print(f"It is {str(unumsameequalnot).lower()} that {unum1} is greater than {unum2}.")

print(" ")

print(f"It is {str(unumsameelesseq).lower()} that {unum1} is less than or equal to {unum2}.")
print(f"It is {str(unumsameegreatereq).lower()} that {unum1} is greater than or equal to {unum2}.")