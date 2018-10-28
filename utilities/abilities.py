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

    def learn_ability(self, unit):
            print(f'{unit.name} learned {self.name}!')
            self.units.append(unit)

    def who_can_use(self):
            return self.units
