# dm is stage dimensions
import string

class Stage():
    def __init__(self, name):
        self.name = name
        self.tiles = []
        self.info = {}
        self.units = []

    def create_stage(self, map_data):
        print(map_data['size'])
        for data in map_data['schema']: # each array in schema
            for x in data:
                print(x)

class Tile():
    def __init__(self, id, height, terrain):
        self.id = id # ex. A1, B5, etc
        self.height = 0
        self.terrain = terrain
        self.vacant = True
        self.traversable = True
        self.effects = {}

    def has_effect(self):
        # returns True if the tile has any effects
        return bool(self.effects)

    def __repr__(self):
        return f'{self.terrain} ({self.id})'


# 0 = black, 1 = green, 2 = gray
# traverse tiles = 1, 2
# obstacle tiles = 0
# include mapping for positioning -- A-Z for cols, 1-26 for rows
# at any moment, you should be able to call a unit's current_pos
# tiles do have properties
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

stage = Stage('Mandalia Plains')

def build_stage():
    print('Stage loaded!')

t = Tile('A1', 0, 'Grass')

stage.create_stage(stage1)
