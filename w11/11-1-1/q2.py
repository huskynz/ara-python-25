class Toy:
    """ Simple class to represent a toy """
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour


class ToyBox:
    """ Simple class to represent a toy box """
    def __init__(self):
        self.all_toys = []

    def add_toy(self, name, colour):
        a_toy = Toy(name, colour)
        self.all_toys.append(a_toy)

    def __str__(self):
        msg = f'The toy box contains the following toys:\n'
        for a_toy in self.all_toys:
            msg += f'A {a_toy.colour.lower()} {a_toy.name}\n'
        return msg
    def get_total_toys(self):
        return len(self.all_toys)