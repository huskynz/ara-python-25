# 1-1-1
# Peter
# peter@husky.nz
# wow

fname = input("Please enter your first name: ")

fnameStripLowerCap = fname.strip().lower().capitalize()

fnum1 = int(input(f"Hi {fnameStripLowerCap}, please enter the first integer: "))
fnum2 = int(input("Please enter the second integer: "))

fnumfinal = fnum1 * fnum2

print(f"{fnameStripLowerCap}, the answer to {fnum1} * {fnum2} is {fnumfinal}")