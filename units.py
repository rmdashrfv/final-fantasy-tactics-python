# from utilities import abilities as abl
# from utilities import equipment as eqt
# from utilities import jobs
# from stages import buildStage as build
from generators.characters import PEOPLE, generate_characters
from random import randint
# print(len(PEOPLE))

# Changing jobs should be like equipping a Job

class Unit():
    def __init__(self, name, **kwargs):
        self.name = name
        self.gender = kwargs.get('gender', 'M')
        self.maxhp = 100
        self.hp = 100
        self.maxmp = 50
        self.mp = 50
        self.strength = 30
        self.status = 'alive'
        self.job = 'Squire'
        self.main_skills = 'Fundaments'
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
        self.jp = {}
        self.ct = 5
        self.move_range = 4
        self.jump = 3
        self.bravery = randint(60, 95)
        self.faith = randint(60, 95)
        self.position = {
            'last_pos': None,
            'current_pos': None
        }
        self.jp['Squire'] = 0

    def __repr__(self):
        return f'{self.name} ({self.job})'

    def change_job(self, new_job):
        old_job = str(self.job)
        self.job = new_job.name
        self.main_skills = new_job.discipline
        # check if key is in units Job points dict
        if self.job not in self.jp.keys():
            self.jp[self.job] = 0
        # map_stats()
        self.maxhp = new_job.maxhp
        self.maxmp = new_job.maxmp
        print(f'{self.name} changed jobs: {old_job} ---> {self.job}')

    def map_stats(self, job):
        # map the stats of the job to the unit
        pass

    def attack(self, tile):
        if not bool(tile.unit):
            return print("Missed!")

        target = tile.unit[0]
        dmg = self.strength
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
        print('----------------------------------------------------------')
        print('NAME   | LEVEL | EXP | JOB  | HP  | MP  | SKILL')
        print('----------------------------------------------------------')
        print(f'[{self.name}] | {self.level} | {self.exp} | {self.job} | {self.maxhp} | {self.maxmp} | {self.main_skills} |')
        print('----------------------------------------------------------')


    def move(self, tile):
        tile_id = tile.tile_id
        path = []
        go_around = 0
        if tile.traversable == False or len(tile.unit) == 1:
            return print('Please select a tile within movement range.')

        coords = self.position['current_pos']
        # check x path 1

        if coords[0] is tile_id[0]:
            print('Not moving left or right')
            x_distance = 0
        else:
            x_distance = ord(coords[0]) - ord(tile_id[0])
            print('x dist is', x_distance)
            if x_distance > 0:
                x_dir = 'left'
                print('Moving left')
            else:
                x_dir = 'right'
                print('Moving right')
            # x_dir = 'left' if x_distance < 0 else 'right'

            # FIRST CHECK Hdiffs on the destination tile
            # check each tile within this range
            # if x_distance is pos check if tiles to the right have a Left Hdiff
            # else (neg) check if tiles to the left have a Right Hdiff
            # check jump height here
                # if there is a

        if coords[1] is tile_id[1]:
            print('not moving up or down')
            y_distance = 0
        else:
            y_distance = int(coords[1]) - int(tile_id[1])
            # check for top and bottom borders

        if y_distance > 0:
            y_dir = 'north'
            print('moving north')
        else:
            y_dir = 'south'
            print('moving south')

        if y_dir == 'north' and 'B' in tile.height_diff:
            print('You can\'t go that way')
        elif y_dir == 'south' and 'T' in tile.height_diff:
            print('You can\'t go this way either')

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


def reward_units(unit1, unit2):
    if unit1.level == unit2.level:
        exp_reward = 1
    else:
        exp_reward = 10
    unit1.exp += exp_reward
    check_levels(unit1)

def reward_jp(unit):
    reward = 10
    unit.jp[unit.job] += reward
    print(f'+{reward}JP >> Total: {unit.jp[unit.job]}')


def check_levels(unit):
    if unit.exp > 2 and unit.exp < 5:
        unit.level = 2
        print(f'{unit.name} leveled up!')

unit1 = Unit('Ramza')
# unit2 = Unit('Delita')
unit3 = Unit('Agrias', gender='F')
# ALL_UNITS.append(unit2)

combatants = generate_characters(PEOPLE, Unit)
# print(combatants)
# print(f'Enemy Units: {combatants[1]}')
# print(f'Ally Units: {combatants[0]}')


# eqt.ARMOR[2].equip_item(unit2)
# print(unit2.hp)

# abl.ABILITIES[0].learn_ability(unit1)
# eqt.WEAPONS[0].equip_item(unit1)
# reward_jp(unit1)
# unit1.change_job(jobs.JOBS['Chemist'])
# print(unit1.report())
# build.stage.units.append(unit1)
# unit1.position['current_pos'] = build.stage.tiles[17].tile_id
# print('current position is', unit1.position['current_pos'])
# unit1.attack(build.stage.tiles[16])
# print('Moving to', build.stage.tiles[18].tile_id)
# unit1.move(build.stage.tiles[18])
# build.stage.tiles[1].info()
# print(unit3.gender)
# reward_jp(unit1)
# unit1.change_job(jobs.JOBS['Squire'])
# reward_jp(unit1)
# reward_jp(unit1)
# print(unit1.jp)
# print(unit1.equipment)
# print(eqt.ARMOR)
# print(unit1.equipment['left'])
