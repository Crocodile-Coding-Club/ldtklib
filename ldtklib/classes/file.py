import json
from .world import LDtkWorldData

class LDtkFile:
    def __init__(self, file_name):
        with open(file_name + ".ldtk", 'r') as file:
            data = json.load(file)
        self.world_data = LDtkWorldData(data)