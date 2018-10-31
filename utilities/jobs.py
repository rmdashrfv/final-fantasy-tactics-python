JOBS = {}

class Job():
    """Jobs are bundles of abilities and specialities that a unit can switch to."""
    def __init__(self, name, **kwargs):
        self.name = name
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

job = Job('Knight', maxhp=110)
print(JOBS)
