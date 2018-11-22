
PEOPLE = [
    {'name': 'Abel', 'gender': 'M'},
    {'name': 'Aleyn', 'gender': 'F'},
    {'name': 'Arnold', 'gender': 'M'},
    {'name': 'Bryce', 'gender': 'M'},
    {'name': 'Bruce', 'gender': 'M'},
    {'name': 'Cain', 'gender': 'M'},
    {'name': 'Bellinda', 'gender': 'F'},
    {'name': 'Celeste', 'gender': 'F'},
    {'name': 'Donovan', 'gender': 'M'},
    {'name': 'Echo', 'gender': 'F'},
    {'name': 'David', 'gender': 'M'},
    {'name': 'Cornelia', 'gender': 'F'},
    {'name': 'Emmet', 'gender': 'M'},
    {'name': 'Girardot', 'gender': 'M'},
    {'name': 'Geoffrey', 'gender': 'M'},
    {'name': 'Gregory', 'gender': 'M'},
    {'name': 'Joyce', 'gender': 'F'},
    {'name': 'Lambert', 'gender': 'M'},
    {'name': 'Rosalind', 'gender': 'F'},
    {'name': 'Sibyl', 'gender': 'F'},
    {'name': 'Vincent', 'gender': 'M'},
    {'name': 'Wilham', 'gender': 'M'},
    {'name': 'Zell', 'gender': 'M'},
    {'name': 'Chloe', 'gender': 'F'}
]

def generate_characters(people, unit):
    allies = []
    enemies = []
    good_guys = 0
    for person in people:
        char = unit(person['name'], gender=person['gender'])
        allies.append(char)
        people.pop()
        good_guys += 1
        if good_guys > 4:
            break

    bad_guys = 0
    for person in people:
        char = unit(person['name'], gender=person['gender'])
        enemies.append(char)
        bad_guys += 1
        if bad_guys > 4:
            break

    return [allies, enemies]
