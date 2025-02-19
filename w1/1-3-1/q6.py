# 1-1-1
# Peter
# peter@husky.nz
# wow


usrfname = input("Please enter your first name: ")

print(f"Hi {usrfname}.")

usrfint = int(input("Please enter the first integer: "))
usrsint = int(input("Please enter the second integer: "))

if usrfint > usrsint:
    numdiff = usrfint - usrsint
else:
    numdiff = usrsint - usrfint

print(f"{usrfname}, the absolute difference between {usrfint} and {usrsint} is {numdiff}.")

