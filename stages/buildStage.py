# dm is stage dimensions
import string

class Stage():
    def __init__(self, name):
        self.name = name
        self.tiles = []
        self.size = []
        self.info = {}
        self.units = []
        self.board = {} # change this to layout

    def create_stage(self, map_data):
        row_count = 1
        for data in map_data['schema']: # each array in schema
            abc = list(string.ascii_uppercase) # new alphabet for each row
            for num in data:
                tile_id = f'{str(abc.pop(0))}{str(row_count)}'
                # print(tile_id)
                if num == 0:
                    tile = Tile(tile_id, 0, 'Void')
                    tile.traversable = False
                elif num == 1:
                    tile = Tile(tile_id, 0, 'Grass')
                elif num == 2:
                    tile = Tile(tile_id, 0, 'Gravel')
                stage.board[tile_id] = tile
                stage.tiles.append(tile)
            row_count += 1
        if map_data['dm'] == '3D':
            print('Building Z Axis')
            for tile in stage.tiles:
                if tile.tile_id in list(map_data['heights'].keys()):
                    print(f'Found {tile}')
                    tile.height_diff = map_data['heights'][tile.tile_id]
                    # print(f'Assigning height to {tile.tile_id}')
                    # print(f'BEFORE: {tile.tile_id} height: {tile.height}')
                    tile.height = tile.height_diff.split('z')[1]
                    # print(tile.height_diff.split('z')[1])
                    # print(f'AFTER: {tile.tile_id} height: {tile.height}')
                    tile.height_diff = tile.height_diff.split('z')[0]
        stage.size = map_data['size']
        # print(stage.board)

    def display_stage(self):
        '''Show the stages tiles that are actually traversable.'''
        col_count = 0
        display = ''
        for k,v in self.board:
            if 'Void' in self.board[k + v].terrain:
                display += ' x '
            else:
                display += f'{self.board[k + v].tile_id} '
            col_count += 1
            if col_count == self.size[0]:
                display += '\n'
                col_count = 0
        print(display)

    def __repr__(self):
        return f'<_{self.name} Stage_>'



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
        return f'<< TILE: {self.tile_id}\n   TYPE: {self.terrain}\n   UNIT: {self.unit or "vacant"}\n   KEY: {self.height_diff}\n   HEIGHT: {self.height} >>'

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
    'heights': {'A1': 'BLz3', 'B1': 'Lz3', 'B2': 'LBz3'}
}

stage2 = {
    'schema': [],
    'size': [5, 11]
}

stage = Stage('Mandalia Plains')

stage.create_stage(stageTest)
stage.display_stage()
# t = stage.tiles[0]
# print(t.info())
# print(stage.tiles)
