class Cookie:
    """ Cookie """
    def __init__(self,brand,flavour,size,calories):
         self.brand = brand.strip().title()
         self.flavour = flavour.strip().title()
         self.size = size
         self.calories = calories
    def __str__(self):
         fname_tital = self.brand
         lname_tital = self.flavour
         msg = f'{fname_tital} makes a ({lname_tital}) flavoured cookie which is {self.size} cm radius and has {self.calories}'

         return msg
    

a_cookie = Cookie('Orio', 'Chocolate', 3, 400)
print(f'Brand: {a_cookie.brand}')
print(f'Flavour: {a_cookie.flavour}')
print(f'Size: {a_cookie.size}')
print(f'Calories: {a_cookie.calories}')
print(a_cookie)