# 1-1-1
# Peter
# peter@husky.nz
# wow

unum = input("Please enter the number: ")
unumstrip = unum.strip()

if unumstrip == ".8":
    unumstrip8="0.8"
    unumstrip.replace(".","",1).isdigit()
    unumstripfloat = float(unumstrip)
    print(f"{unumstrip8} is a valid number.")
elif unumstrip.replace(".","",1).isdigit():
    unumstripfloat = float(unumstrip)
    print(f"{unumstrip} is a valid number.")
else:
    print(f"{unumstrip} is not a valid number.")