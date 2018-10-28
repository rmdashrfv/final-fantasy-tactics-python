class Equipment():
    pass


class Weapon():
    def __init__(self, name, wp_type, atk, defense):
        self.name = name
        self.wp_type = wp_type
        self.atk = atk
        self.defense = defense

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