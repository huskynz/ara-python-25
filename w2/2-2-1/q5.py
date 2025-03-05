# 1-1-1
# Peter
# peter@husky.nz
# wow

beachtoday = input("Should we go to the beach? (y/n): ")
issaturday = input("Is it Saturday? (y/n): ")
issunday = input("Is it Sunday? (y/n): ")
istideout = input("Is the tide out? (y/n): ")

beachtodaystrip = beachtoday.strip()
issaturdaystrip = issaturday.strip()
issundaystrip = issunday.strip()
beachtodaystrip = istideout.strip()

beachtodaylower = beachtodaystrip.lower()
issaturdaylower = issaturdaystrip.lower()
issundaylower = issundaystrip.lower()
istideoutlower = beachtodaystrip.lower()

beachtodayY = beachtodaylower.startswith("y")
issaturdayY = issaturdaylower.startswith("y")
issundayY = issundaylower.startswith("y")
istideoutY = istideoutlower.startswith("y")

vaildbeachday = beachtoday is True and istideoutY is False and issaturdayY is True or issundayY is True and not issundayY and issaturdayY is True
vaildbeachdaylow = str(vaildbeachday).lower()

print(" ")
print(f"It is {vaildbeachdaylow} that we can go to the beach today.") 