class Toy:
    """ Simple class to represent a toy """
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour


class ToyBox:
    """ Simple class to represent a toy box """
    def __init__(self):
        self.all_toys = []

    def add_toy(self, name, colour, cost):
        a_toy = Toy(name, colour)
        self.all_toys.append(a_toy)
        a_toy.cost = cost

    def __str__(self):
        msg = f'The toy box contains the following toys:\n'
        for a_toy in self.all_toys:
            msg += f'A {a_toy.colour.lower()} {a_toy.name}\n'
        return msg
    def get_total_toys(self):
        return len(self.all_toys)
    def get_total_cost(self):
        total_cost = 0
        for a_toy in self.all_toys:
            total_cost += a_toy.cost
        return total_cost