import json
from .world import LDtkWorldData

class LDtkFile:
    def __init__(self, file_relative_path):
        with open(file_relative_path, 'r') as file:
            data = json.load(file)
        self.world_data = LDtkWorldData(data)