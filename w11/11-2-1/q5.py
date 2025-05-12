class Toy:
    """ Simple class to represent a toy """
    def __init__(self, name, colour, toy_type):
        self.name = name
        self.colour = colour
        self.toy_type = toy_type

    def __str__(self):
        return f'{self.colour} {self.name}'

    def __repr__(self):
        return f"'{self.name}'"


class ToyBox:
    """ Simple class to represent a toy box """
    def __init__(self):
        self.all_toys = []

    def add_toy(self, name, colour, cost, toy_type):
        a_toy = Toy(name, colour, toy_type)
        a_toy.cost = cost
        self.all_toys.append(a_toy)

    def __str__(self):
        if self.get_total_toys() == 0:
            return 'The toy box is empty.'
        
        msg = f'The toy box contains {self.get_total_toys()} toy{"s" if self.get_total_toys() > 1 else "s"}\n'
        for a_toy in self.all_toys:
            msg += f'A {a_toy.colour.lower()} {a_toy.toy_type.lower()} called {a_toy.name} which cost ${a_toy.cost:.2f}\n'
        msg += f'Total cost: ${self.get_total_cost():.2f}'
        return msg

    def get_total_toys(self):
        return len(self.all_toys)

    def get_total_cost(self):
        return sum(a_toy.cost for a_toy in self.all_toys)

    def get_cheapest_toy(self):
        if not self.all_toys:
            return "The toy box is empty."
        return min(self.all_toys, key=lambda toy: toy.cost)

    def find_toy(self, name):
        for toy in self.all_toys:
            if toy.name.lower() == name.lower():
                return toy
        return False

    def remove_toy(self, name):
        toy = self.find_toy(name)
        if toy:
            self.all_toys.remove(toy)
            return True
        return False

    def get_by_toy_type(self, toy_type):
        if self.get_total_toys() == 0:
            return (False, "The toy box is empty.")
        
        matching_toys = []
        for toy in self.all_toys:
            if toy.toy_type.lower() == toy_type.lower():
                matching_toys.append(toy)
        
        if matching_toys:
            return (True, matching_toys)
        return (False, f"There are no toys of type {toy_type} in the toybox")