ABILITIES = []


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

# range 0 = the person using the ability
# FUNDAMENTS
# Damage=PhysicalAttackx(randomnumberfrom1toPWR)
# name, damage, rng, jp_cost, mp_cost, ct_cost
throw_stone = Ability('Throw Stone', 10, 4, 10, 0, 5)
throw_stone = Ability('Throw Stone', 10, 4, 10, 0, 5)
accumulate = Ability('Accumulate', 0, 0, 0, 0, 5)
tailwind = Ability('Tailwind', 1, 3, 0, 0, 5) # only available to Ramza

#
