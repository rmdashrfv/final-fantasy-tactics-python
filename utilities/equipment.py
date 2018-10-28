class Equipment():
    print('Equipment class')


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
    print('armor')

class Shield():
    print('shield')

class Helm():
    print('helmet')

class Shoes():
    print('shoes')