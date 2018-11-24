ABILITIES = []


# action, reaction, support, movement
class Ability():
    def __init__(self, name, damage, rng, jp_cost, mp_cost, ct_cost):
        self.name = name
        self.discipline = None
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

#
