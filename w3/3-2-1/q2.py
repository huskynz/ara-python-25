# 1-1-1
# Peter
# peter@husky.nz
# wow

ufname = input("Please enter your first name: ").strip().title()

uage = int(input(f"Hi {ufname}, please enter your age in years: "))


if (uage % 2) == 0:
    print(f"{ufname}, {uage} is an even number of years.")
else:
    print(f"{ufname}, {uage} is an odd age.")