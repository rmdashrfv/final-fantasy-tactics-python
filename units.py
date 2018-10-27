class Unit():
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.mp = 50
        self.strength = 30
        self.defense = 5
        self.status = 'alive'
        self.job = 'Squire'
        self.speed = 10
        self.abilities = []
        self.equipment = {
            'left': None,
            'right': None,
            'helm': None,
            'armor': None,
            'shoes': None
        }

    def attack(target):
        print(f'{self.name} attacked the target!')