class Cookie:
    """ Cookie """
    def __init__(self,brand,flavour,size,calories):
         self.all_cookies = []
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
    def __str__(self):
        msg = f'This jar has {len(self.all_cookies)} cookies with {1800} calories\n'
        for all_cookies in self.all_cookies:
            msg += f'{all_cookies.brand} makes a ({all_cookies.flavour}) flavoured cookie which is {all_cookies.size} cm radius and has {all_cookies.calories}\n'
        return msg
    def get_total_cookies(self):
        return(len(self.all_cookies))
    def find_cookie(self, brand):
        for all_cookies in self.all_cookies:
            if all_cookies.brand.lower() == brand.lower():
                msg = f'{all_cookies.brand} makes a ({all_cookies.flavour}) flavoured cookie which is {all_cookies.size} cm radius and has {all_cookies.calories}\n'
                return msg
        return False
    def get_total_calories(self):
        return sum(all_cookies.calories for all_cookies in self.all_cookies)