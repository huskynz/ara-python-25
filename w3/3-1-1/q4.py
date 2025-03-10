# 1-1-1
# Peter
# peter@husky.nz
# wow

unum = input("Please enter the number: ")
unumstrip = unum.strip()

uisnum = unumstrip.isdigit()

uisfloat = unumstrip.isinteger()

if uisnum == True:
    print(f"{unumstrip} is a valid number.")
else:
    print(f"{unumstrip} is not a valid number.")