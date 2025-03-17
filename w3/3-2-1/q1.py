# 1-1-1
# Peter
# peter@husky.nz
# wow

# 1-1-1
# Peter
# peter@husky.nz
# wow

ufname = input("Please enter your first name: ").strip().capitalize()

unum1 = input(f"Hi {ufname}. Please enter the first number: ")

unum2 = input(f"Thanks {ufname}. Please enter the second number: ")


if unum1 is unum2:
    print(f"{unum1} is equal to {unum2}")
elif unum1 > unum2:
    print(f"{unum1} is greater than {unum2}")
elif unum1 < unum2:
    print(f"{unum1} is less than {unum2}")
