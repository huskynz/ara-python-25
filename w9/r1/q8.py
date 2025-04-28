# 1-1-1
# Peter
# peter@husky.nz
# wow

fstartletter = "A"
fendletter = "n"

fname = input("Please enter your first name: ")


fnamestrip = fname.strip().lower()
fnamecap = fnamestrip.title()

fnameEnd = fnamecap.endswith(fendletter)
fnameStartWith = fnamecap.startswith(fstartletter)

if fnameEnd == True and fnameStartWith == True:
    print(f"Hi {fnamecap}, your first name starts with the letter {fstartletter}.")
    print(f"Hi {fnamecap}, your first name ends with the letter {fendletter}.")
elif fnameStartWith == True and fnameEnd == False or fnameEnd == True and fnameStartWith == False:
    print(f"Hi {fnamecap}, your first name starts with the letter {fstartletter}.")
    print(f"Hi {fnamecap}, your first name does not end with the letter {fendletter}.")

elif fnameEnd == True and fnameStartWith == False:
    print(f"Hi {fnamecap}, your first name does not start with the letter {fstartletter}.")
    print(f"Hi {fnamecap}, your first name ends with the letter {fendletter}.")
elif fnameEnd == False and fnameStartWith == False:
    print(f"Hi {fnamecap}, your first name does not start with the letter {fstartletter}.")
    print(f"Hi {fnamecap}, your first name does not end with the letter {fendletter}.")