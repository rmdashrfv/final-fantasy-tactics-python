DISCIPLINES = {}
ABILITIES = []

class Discipline():
    def __init__(self, name):
        self.name = name
        self.abilities = {
            'action': {},
            'reaction':  {},
            'support': {},
            'movement': {}
        }
        DISCIPLINES[name] = self

    def __repr__(self):
        return f'{self.name}'


# action, reaction, support, movement
class Ability():
    def __init__(self, name, damage, rng, jp_cost, mp_cost, ct_cost):
        self.name = name
        self.params = {
            'dmg': damage,
            'rng': rng,
            'jp_cost': jp_cost,
            'mp_cost': mp_cost,
            'ct_cost': ct_cost
        }
        self.units = []
        ABILITIES.append(self)

    def learn_ability(self, unit):
            print(f'{unit.name} learned {self.name}!')
            self.units.append(unit)

    def who_can_use(self):
            return self.units

    def __repr__(self):
        return f'{self.name} ({self.discipline})'

# range 0 = use this on yourself
# FUNDAMENTS
# Damage=PhysicalAttackx(randomnumberfrom1toPWR)
# name, damage, rng, jp_cost, mp_cost, ct_cost
throw_stone = Ability('Throw Stone', damage=10, rng=4, jp_cost=10, mp_cost=0, ct_cost=5)
accumulate = Ability('Accumulate', damage=0, rng=0, jp_cost=0, mp_cost=0, ct_cost=5)
tailwind = Ability('Tailwind', damage=1, rng=3, jp_cost=0, mp_cost=0, ct_cost=5) # only available to Ramza

disciplines = "Fundaments, Item, Arts of War, Aim, White Magick, Black Magick, Martial Arts, Time Magick, Summon, Steal, Speechcraft, Mystic Arts, Geomancy, Jump, Iaido, Throw, Arithmeticks, Mystic Arts, Bardsong, Dance, Mimic, Darkness, Huntcraft"

for disc in disciplines.split(', '):
    new_discipline = Discipline(disc)
    print(disc)
#
del disc

print(DISCIPLINES)

for abl in ABILITIES:
    DISCIPLINES['Fundaments'].abilities['action'][abl.name] = abl

print(DISCIPLINES['Fundaments'].abilities['action'].keys())
