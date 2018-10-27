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

    def __repr__(self):
        return f'{self.name} >> {self.job} ({self.hp})HP'

    def change_job(self, new_job):
        old_job = str(self.job)
        self.job = str(new_job).upper()
        print(f'{self.name} changed jobs: {old_job} ---> {self.job}')

    def attack(self, target):
        dmg = self.strength - target.defense
        target.hp - dmg
        print(f'{self.name} attacked {target.name}!')
        print(f'{target.name} lost {dmg} HP')
        if target.hp <= 0:
            target.status = 'felled'
            print(f'{target.name} has fallen!')
        elif target.hp < target.hp / 2:
            target.status = 'critical'
            print(f'{target.name} is in critical condition!')


class Chemist(Unit):
    def __init__(self):
        super().hp -= 25
        self.strength -= 3
        self.defense += 10

    def __repr__(self):
        return(f'{self}')


unit1 = Unit('Ramza')
unit2 = Unit('Delita')

unit1.attack(unit2)
unit1.change_job(Chemist())