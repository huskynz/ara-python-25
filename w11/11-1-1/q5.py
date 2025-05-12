class Toy:
    """ Simple class to represent a toy """
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

    def __str__(self):
        return f'{self.colour} {self.name}'

    def __repr__(self):
        return f'Toy(name="{self.name}", colour="{self.colour}")'


class ToyBox:
    """ Simple class to represent a toy box """
    def __init__(self):
        self.all_toys = []

    def add_toy(self, name, colour, cost):
        a_toy = Toy(name, colour)
        a_toy.cost = cost
        self.all_toys.append(a_toy)

    def __str__(self):
        if self.get_total_toys() == 0:
            return 'The toy box is empty.'
        
        msg = f'The toy box contains {self.get_total_toys()} toy{"s" if self.get_total_toys() > 1 else ""}\n'
        for a_toy in self.all_toys:
            msg += f'A {a_toy.colour.lower()} {a_toy.name} which cost ${a_toy.cost:.2f}\n'
        msg += f'Total cost: ${self.get_total_cost():.2f}'
        return msg

    def get_total_toys(self):
        return len(self.all_toys)

    def get_total_cost(self):
        return sum(a_toy.cost for a_toy in self.all_toys)

    def get_cheapest_toy(self):
        if not self.all_toys:
            return None
        return min(self.all_toys, key=lambda toy: toy.cost)
