from .level import LDtkLevelData

class LDtkWorldData:
    def __init__(self, world_data:dict):
        self.identifier = world_data.get("identifier")
        self.iid = world_data.get("iid")
        self.levels: list[LDtkLevelData] = []
        for level in world_data.get("levels"):
            self.levels.append(LDtkLevelData(level))
        self.worldGridHeight = world_data.get("worldGridHeight")
        self.worldGridWidth = world_data.get("worldGridWidth")
        self.worldLayout = world_data.get("worldLayout")