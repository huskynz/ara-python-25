# 1-1-1
# Peter
# peter@husky.nz
# wow

uletter="Q"

uword=input(f"Please enter a word that starts with upper case {uletter}: ")
uletterfch=uword[:1]

uletterstart= uletter in uletterfch

uletterstarttostr = str(uletterstart)

uletterstartlow = uletterstarttostr.lower()

print(f"It is {uletterstartlow} that {uword} starts with upper case {uletter}.")