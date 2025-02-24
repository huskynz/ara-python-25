# 1-1-1
# Peter
# peter@husky.nz
# wow


ufname=input("Please enter your first name: ")

ufnamestrip=ufname.strip()
ufnamecap=ufnamestrip.title()


ulname=input(f"{ufnamecap}, please enter your last name: ")

ulnamestrip=ulname.strip()
ulnamecap=ulnamestrip.title()

usen=input(f"{ufnamecap}, please enter a sentence: ")

usenstrip=usen.strip()
usencap=usenstrip.capitalize()

usencnt=len(usencap)

usencntfl= usenstrip[0]
usencntll= usenstrip[-1]


print(f"Report for {ufnamecap + ' ' + ulnamecap}'s sentence of {usencnt} characters.")

print(f"First character: {usencntfl}")
print(f"Last character: {usencntll.lower()}")
