ALL_WEAPONS = []

class Equipment():
    pass

class Weapon():
    def __init__(self, name, wp_type, atk, defense):
        self.name = name
        self.wp_type = wp_type
        self.atk = atk
        self.defense = defense
        ALL_WEAPONS.append(self)
    

    def __repr__(self):
        return f'{self.name} ({self.wp_type})'

    def equip_item(self, unit):
        unit.equipment['left'] = self
        print(f'{self.name} equipped')


class Armor():
    pass

class Shield():
    pass

class Helm():
    pass

class Shoes():
    pass

longsword = Weapon('Longsword', 'sword', 10, 0)
iron_sword = Weapon('Iron Sword', 'sword', 15, 0)