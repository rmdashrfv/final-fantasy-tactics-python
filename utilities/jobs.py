from abilities import ABILITIES as abl
print(abl)
JOBS = {}

class Job():
    """Jobs are bundles of abilities and specialities that a unit can switch to."""
    def __init__(self, name, **kwargs):
        self.name = name
        self.discipline = kwargs.get('disc', 'Fundaments')
        self.maxhp = kwargs.get('maxhp', 100)
        self.hp = self.maxhp
        self.maxmp = kwargs.get('maxmp', 50)
        self.mp = self.maxmp
        self.speed = kwargs.get('speed', 10)
        self.move_range = kwargs.get('move_range', 4)
        self.jump = kwargs.get('jump', 3)
        JOBS[name] = self

    def __repr__(self):
        return f'[{self.name}]'

job = Job('Squire', maxhp=100)
job = Job('Chemist', maxhp=70, disc='Item', move_range=3)
job = Job('Knight', maxhp=120, disc='Arts of War')
job = Job('Archer', maxhp=100, disc='Aim')
job = Job('White Mage', maxhp=100, disc='White Magick')
job = Job('Black Mage', maxhp=100, disc='Black Magick')
job = Job('Monk', maxhp=100, disc='Martial Arts')
job = Job('Time Mage', maxhp=100, disc='Time Magick')
job = Job('Summoner', maxhp=100, disc='Summon')
job = Job('Thief', maxhp=100, disc='Steal')
job = Job('Orator', maxhp=100, disc='Speechcraft')
job = Job('Mystic', maxhp=100, disc='Mystic Arts')
job = Job('Geomancer', maxhp=100, disc='Geomancy')
job = Job('Dragoon', maxhp=100, disc='Jump')
job = Job('Samurai', maxhp=100, disc='Iaido')
job = Job('Ninja', maxhp=100, disc='Throw')
job = Job('Calculator', maxhp=100, disc='Arithmeticks')
job = Job('Mystic', maxhp=100, disc='Mystic Arts')
job = Job('Bard', maxhp=100, disc='Bardsong')
job = Job('Dancers', maxhp=100, disc='Dance')
job = Job('Mime', maxhp=100, disc='Mimic')
job = Job('Dark Knight', maxhp=100, disc='Darkness')
job = Job('Game Hunter', maxhp=100, disc='Huntcraft')
# print(JOBS)
