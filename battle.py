from units import ALL_UNITS
from stages.buildStage import stage as field
# print(stage.tiles)

battleTime = True
turn_count = 0
choices = "[ 1 = 'Move' | 2 = 'Act' | 3 = 'Wait' | 4 = 'Status' ]"
while battleTime and turn_count < 100:
    for unit in ALL_UNITS:
        unit.ct += unit.speed
        if unit.ct >= 100:
            print("It's your turn, ", unit.name)
            act = input(f'What will you do, {unit.name}?\n{choices}')
            if act == '2':
                unit.ct -= 55
                target = input('Where will you attack? N/S/E/W?')
                if target == 'N':
                    unit.attack(field.tiles[0])
            elif act == '3':
                print('waiting ...')
                unit.ct -= 25
            elif act == '1':
                unit.ct -= 35
                # choice = input('Select a tile and press X to move there.')
                choice = input(f'Select a tile by entering its location.\n {unit.name}\'s move range: {unit.move_range}')
                # unit.move(field)
                unit.position['current_pos'] = choice
    print(turn_count)
    turn_count += 1
