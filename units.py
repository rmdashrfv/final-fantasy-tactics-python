from utilities import abilities as abl
from utilities import equipment as eqt
from stages import buildStage as build
build.build_stage()

class Unit():
    def __init__(self, name):
        self.name = name
        self.maxhp = 100
        self.hp = 100
        self.maxmp = 50
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
        self.level = 1
        self.exp = 0
        self.jp = 0
        self.ct = 5
        self.move = 3

    def __repr__(self):
        return f'{self.name} >> {self.job} ({self.hp})HP'

    def change_job(self, new_job):
        old_job = str(self.job)
        self.job = str(new_job).upper()
        self.hp = new_job.hp
        self.mp = new_job.mp
        print(f'{self.name} changed jobs: {old_job} ---> {self.job}')

    def attack(self, target):
        dmg = self.strength - target.defense
        target.hp = target.hp - dmg
        print(f'{self.name} attacked {target.name}!')
        reward_units(self, target)
        # print(f'{target.name} lost {dmg} HP')
        if target.hp < (target.maxhp / 2) and target.hp > 0:
            target.status = 'critical'
            print(f'{target.name} is in critical condition!')
        elif target.hp <= 0:
            target.status = 'felled'
            print(f'{target.name} has fallen!')

    def report(self):
        print(f'[{self.name}]\nLV: {self.level}\nEXP: {self.exp}\nJP: {self.jp}')


# Classes use inheritance to prevent me from writing all stats for each subclass
class Chemist():
    def __init__(self):
        self.hp = 75
        self.strength = 15
        self.defense = 3
        self.mp = 15


def reward_units(unit1, unit2):
    if unit1.level == unit2.level:
        exp_reward = 1
    else:
        exp_reward = 10
    unit1.exp += exp_reward
    check_levels(unit1)


def check_levels(unit):
    if unit.exp > 2 and unit.exp < 5:
        unit.level = 2
        print(f'{unit.name} leveled up!')
    
unit1 = Unit('Ramza')
unit2 = Unit('Delita')


# eqt.ARMOR[2].equip_item(unit2)
unit1.attack(unit2)
unit1.attack(unit2)
unit1.attack(unit2)
unit1.attack(unit2)
print(unit2.hp)

abl.ABILITIES[0].learn_ability(unit1)
eqt.WEAPONS[0].equip_item(unit1)

unit1.report()
# print(unit1.equipment)
# print(eqt.ARMOR)
# print(unit1.equipment['left'])