# Example code from the PowerPoint

class Toy:
    """ """
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour


class ToyBox:
    """ """
    def __init__(self):
        self.all_toys = []

    def add_toy(self, name, colour):
        a_toy = Toy(name, colour)
        self.all_toys.append(a_toy)

    def __str__(self):
        msg = f'The toy box contains the following toys:\n'
        for a_toy in self.all_toys:
            msg += f'{a_toy.name}\n'
        return msg


the_box = ToyBox()
print(the_box)
the_box.add_toy('Big Ted', 'Grey')
the_box.add_toy('Buzz Lightyear', 'Yellow')
the_box.add_toy('Rocking horse', 'Wooden')
print(the_box)


