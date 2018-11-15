WEAPONS = []
ARMOR = []

class Equipment():
    pass

class Weapon():
    def __init__(self, name, wp_type, atk):
        self.name = name
        self.wp_type = wp_type
        self.atk = atk
        WEAPONS.append(self)
    

    def __repr__(self):
        return f'{self.name} ({self.wp_type})'

    def equip_item(self, unit):
        unit.equipment['left'] = self
        unit.strength += self.atk
        print(f'{self.name} equipped')


class Armor():
    def __init__(self, name, hp, mp, arm_type):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.arm_type = arm_type
        ARMOR.append(self)
    
    def __repr__(self):
        return f'{self.name} ({self.arm_type})'

    def equip_item(self, unit):
        unit.equipment['armor'] = self
        unit.maxhp += self.hp
        unit.maxmp += self.mp
        unit.hp += self.hp
        unit.mp += self.mp
        print(f'{self.name} equipped')


class Shield():
    pass

class Helm():
    pass

class Shoes():
    pass

longsword = Weapon('Longsword', 'Sword', 10)
iron_sword = Weapon('Iron Sword', 'Sword', 15)
leather = Armor('Leather Armor', 10, 0, 'Heavy')
linen_cur = Armor('Linen Cuirass', 20, 0, 'Heavy')
bronze_armor = Armor('Bronze Armor', 30, 0, 'Heavy')
leather = Armor('Chain Mail', 40, 0, 'Heavy')
linen_cur = Armor('Mythril', 50, 0, 'Heavy')

longbow = Weapon('Long Bow', 'Bow', 4)
silverbow = Weapon('Silver Bow', 'Bow', 5)
icebow  = Weapon('Ice Bow', 'Bow', 5)