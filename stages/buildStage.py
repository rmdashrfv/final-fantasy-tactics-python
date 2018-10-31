# dm is stage dimensions
import string

class Stage():
    def __init__(self, name):
        self.name = name
        self.tiles = []
        self.info = {}
        self.units = []

    def create_stage(self, map_data):
        row_count = 1
        for data in map_data['schema']: # each array in schema
            abc = list(string.ascii_uppercase) # new alphabet for each row
            for num in data:
                tile_id = f'{str(abc.pop(0))}{str(row_count)}'
                # print(tile_id)
                if num == 0:
                    terrain = 'void'
                elif num == 1:
                    terrain = 'Grass'
                elif num == 2:
                    terrain = 'Gravel'
                tile = Tile(tile_id, 0, terrain)
                stage.tiles.append(tile)
            row_count += 1
        if map_data['dm'] == '3D':
            print('Building Z Axis')
            for tile in stage.tiles:
                if tile.tile_id in list(map_data['heights'].keys()):
                    print(f'Found {tile}')



class Tile():
    def __init__(self, tile_id, height, terrain):
        # height differentials in directions
        self.tile_id = tile_id # ex. A1, B5, etc
        self.height = 0
        self.terrain = terrain
        self.vacant = True
        self.traversable = True # false = impassable
        self.height_diff = ''
        self.unit = []
        self.effects = {}

    def has_effect(self):
        # returns True if the tile has any effects
        return bool(self.effects)

    def info(self):
        print(f'POS: {self.tile_id}\nTYPE: {self.terrain}\nUNIT: {self.unit[0]}')

    def __repr__(self):
        return f'({self.tile_id}) {self.terrain}'


# 0 = black, 1 = green, 2 = gray
# traverse tiles = 1, 2
# obstacle tiles = 0
# include mapping for borders of height
# remember all possible height diff combinations
# include mapping for positioning -- A-Z for cols, 1-26 for rows
# at any moment, you should be able to call a unit's current_pos
# tiles do have properties
stage1 = {
    'schema': [[2, 2, 2, 0, 1, 1, 1, 1, 2, 2, 2, 1],
               [1, 1, 2, 0, 0, 1, 2, 0, 1, 1, 1, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
    'size': [12, 13],
    'dm': '2D',
    'heights': {}
}

stageTest = {
    'schema': [[2, 2, 2, 0, 1],
               [1, 2, 1, 0, 1],
               [1, 2, 1, 1, 2],
               [1, 1, 2, 0, 2]],
    'size': [5, 4],
    'dm': '3D',
    'heights': {'A1': 'TRBz3', 'B1': 'Lz3', 'B2': 'LBz3'}
}

stage2 = {
    'schema': [],
    'size': [5, 11]
}

stage = Stage('Mandalia Plains')

stage.create_stage(stageTest)
print(stage.tiles)
