from utilities import abilities as abl
from utilities import equipment as eqt
from utilities import jobs
from stages import buildStage
from generators.characters import PEOPLE, generate_characters
from random import randint
from units import Unit

print("Modules loaded successfully!")

unit1 = Unit('Ramza')
unit2 = Unit('Agrias', gender='F')
unit3 = Unit('Delita')
stage = buildStage.stage

# tile example = stage.board[tile_id]
print(stage.board['A1'])
allies = [unit1, unit3]
enemies = [unit2]
all_units = [unit1, unit2, unit3]

def check_survivors(good, bad):
    dead_good_units = 0
    for unit in good:
        if unit.status == 'felled':
            dead_good_units += 1
        if dead_good_units == len(good):
            return 'GAME OVER'

    del unit
    dead_bad_units = 0
    for unit in bad:
        if unit.status == 'felled':
            dead_bad_units += 1
        if dead_bad_units == len(bad):
            return 'YOU ARE VICTORIOUS'


victory_msg = '''CONGRATULATIONS!

This battle is complete!
'''

defeat_msg = '''GAME OVER ...'''



def start_battle(allies, enemies):
    battleTime = True
    turn_count = 0
    choices = "[ 1 = 'Move' | 2 = 'Act' | 3 = 'Wait' | 4 = 'Status' ]\n"
    while battleTime and turn_count < 100:
        for unit in all_units:
            unit.ct += unit.speed
            if unit.ct >= 100:
                print("It's your turn, ", unit.name)
                act = input(f'What will you do, {unit.name}?\n{choices}')
                if act == '2':
                    unit.ct -= 55
                    target = input('Where will you attack? N/S/E/W?')
                    if target == 'N':
                        standing = unit.position['current_pos']
                        unit.attack(stage.tiles[0])
                elif act == '3':
                    print('waiting ...\n\n')
                    allies[0].hp -= 25
                    print(allies[0].hp)
                    if allies[0].hp <= 0:
                        allies[0].status = 'felled'
                        allies[1].hp -= 30
                        if allies[1].hp <= 0:
                            allies[1].status = 'felled'
                    unit.ct -= 25
                elif act == '1':
                    unit.ct -= 35
                    # choice = input('Select a tile and press X to move there.')
                    print(f'''===============\n
                        {stage.display_stage()}
                    ''')
                    choice = input(f'Select a tile by entering its location.\n {unit.name}\'s move range: {unit.move_range}')
                    # unit.move(stage)
                    if choice not in stage.board.keys():
                        print('Please select a tile within range')
                        choice = input(f'Select a tile by entering its location.\n {unit.name}\'s move range: {unit.move_range}')
                    unit.position['current_pos'] = choice

                turn_count += 1
        if check_survivors(allies, enemies) == 'YOU ARE VICTORIOUS':
            print(victory_msg)
            battleTime = False
        elif check_survivors(allies, enemies) == 'GAME OVER':
            print(defeat_msg)
            battleTime = False
        else:
            pass
