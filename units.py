from utilities import abilities as abl
from utilities import equipment as eqt
from stages import buildStage as build

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
        self.move_range = 3
        self.jump = 1
        self.position = {
            'last_pos': None,
            'current_pos': None
        }

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

    def move(self, tile):
        # make sure a unit can't move off the screen!!!
        # on stageload set last_pos and current_pos
        # need current_tile
        # unit moves to a given tile
        # need to determine distance
        # check if tile occupied and traversable
        tile_id = tile.tile_id
        coords = self.position['current_pos']
        # go_around is the additonal dist a unit must walk in the event of a height differential
        go_around = 0
        # self.position['last_pos'] = tile_id
        if coords[0] is tile_id[0]:
            print('Moving down')
            x_distance = 0
        else:
            print('Moving across')
            x_distance = ord(coords[0]) - ord(tile_id[0])
            # FIRST CHECK Hdiffs on the destination tile
            # check each tile within this range
            # if x_distance is pos check if tiles to the right have a Left Hdiff
            # else (neg) check if tiles to the left have a Right Hdiff
            # check jump height here
                # if there is a

        if coords[1] is tile_id[1]:
            print('Moving up')
            y_distance = 0
        else:
            print('x')
            y_distance = int(coords[1]) - int(tile_id[1])
            # check for top and bottom borders

        distance = abs(x_distance) + abs(y_distance) # add go_around
        print(f'{self.name} moving {distance} places')

        if distance > self.move_range:
            print('You can\'t move that far')

        tile.vacant = False
        tile.unit.append(self)

        # calculate distance
        # if distance > self.move:
            # ....
        # update current position
        self.position['current_pos'] = tile_id
        print(self.position)


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

# abl.ABILITIES[0].learn_ability(unit1)
# eqt.WEAPONS[0].equip_item(unit1)
build.stage.units.append(unit1)
print(build.stage.tiles[7].tile_id)
unit1.position['current_pos'] = build.stage.tiles[0].tile_id
unit1.move(build.stage.tiles[7])
build.stage.tiles[7].info()
# print(unit1.equipment)
# print(eqt.ARMOR)
# print(unit1.equipment['left'])
