# party can only have 24 units
# party stores all gil
# party stores all acquired items and quantities

class Party:
    def __init__(self, items, units, gil):
        self.items = {} # get an item, count its quantity
        self.units = [] # len to get count
        self.gil = 0

    def welcome_new_unit(self, unit):
        if len(self.units) < 24:
            self.units.append(unit)
        else:
            print('The party is already full.')

    def dismiss(self, unit):
        # delete unit from array
        pass
