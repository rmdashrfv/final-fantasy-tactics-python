# dm is stage dimensions

class Stage():
    def __init__(self, name, tiles, size):
        self.name = name
        self.tiles = tiles
        self.size = size
        self.units = []


# 0 = black, 1 = green, 2 = gray
stage1 = {
    'schema': [[2, 2, 2, 0, 1, 1, 1, 1, 2, 2, 2, 1],
               [1, 1, 2, 0, 0, 1, 2, 0, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
    'size': [12, 13]
}

stage2 = {
    'schema': [],
    'size': [5, 11]
}

stage = Stage('Mandalia Plains', stage1['schema'], stage1['size'])

def build_stage():
    print('Stage loaded!')