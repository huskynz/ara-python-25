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