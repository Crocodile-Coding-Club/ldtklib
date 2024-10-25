from .layer import LDtkLayerData

class LDtkLevelData:
    def __init__(self, level_data):
        self.identifier = level_data.get("identifier")
        self.iid = level_data.get("iid")
        self.uid = level_data.get("uid")
        self.layerInstances: list[LDtkLayerData] = []
        for layer in level_data.get("layerInstances"):
            self.layerInstances.append(LDtkLayerData(layer))