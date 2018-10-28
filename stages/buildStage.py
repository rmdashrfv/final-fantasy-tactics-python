# dm is stage dimensions

class Stage():
    def __init__(self, name, dm):
        self.name = name
        self.dm = dm
        self.units = []


def build_stage():
    print('Stage loaded!')