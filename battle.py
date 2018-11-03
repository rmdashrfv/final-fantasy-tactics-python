from units import ALL_UNITS
from stages.buildStage import stage as field
# print(stage.tiles)

battleTime = True
turn_count = 0
choices = "[ 1 = 'Move' | 2 = 'Attack' | 3 = 'Wait' ]"
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
    print(turn_count)
    turn_count += 1
