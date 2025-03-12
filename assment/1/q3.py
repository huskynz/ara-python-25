# 1-1-1
# Peter
# peter@husky.nz
# wow

MinLow = 0
MinPass = 60
MeritMark = 90
MaxMark = 100


Ass1Mark = input("Enter your mark for assessment 1: ")

try:

    Ass1Markint = int(Ass1Mark)

    Ass1MarkVaild = Ass1Markint >= 0 and  Ass1Markint <= 100

    if Ass1MarkVaild == True and Ass1Markint >= 90:
        print(f"Well done! {Ass1Mark} gained you a Merit!")
    elif Ass1MarkVaild == True and Ass1Markint >= 60:
        print(f"Congratulations, scoring {Ass1Mark} gained you a Pass grade.")
    elif Ass1MarkVaild == False:
        print(f"The assessment mark is not in the range {MinLow} to {MaxMark}.")
    elif Ass1MarkVaild == True and Ass1Markint < 60:
        print("You received a Fail grade for the course due to not getting the minimum mark for assessment 1.")
except ValueError:
    print("The assessment mark needs to be an integer.")