class Cookie:
    """ Cookie """
    def __init__(self,brand,flavour,size,calories):
         self.brand = brand.strip().title()
         self.flavour = flavour.strip().title()
         self.size = size
         self.calories = calories

class Jar:
    """ JAR """
    def __init__(self):
        self.all_cookies = []
    def add_cookie(self,brand,flavour,size,calories):
        self.all_cookies.append(Cookie(brand, flavour, size, calories))
        return True