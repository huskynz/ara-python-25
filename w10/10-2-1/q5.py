# 1-1-1
# Peter
# peter@husky.nz
# wow

class Cat:
    """
    This class represents a Cat with a name and age.
    """
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name.strip().title()
        self.age: int = int(str(age).strip())
        
    def __str__(self) -> str:
        return f"{self.name}, the awesome cat is {self.age} year{'s' if self.age != 1 else ''} old"