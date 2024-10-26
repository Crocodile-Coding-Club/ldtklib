from .tile import LDtkTileData
from .entity import LDtkEntityData

class LDtkLayerData:
    def __init__(self, layer_data: dict):
        self.layer_id = layer_data.get("iid")
        self.level_definition_id = layer_data.get("layerDefUid")
        self.level_id = layer_data.get("levelId")
        self.x_offset = layer_data.get("pxOffsetX")
        self.y_offset = layer_data.get("pxOffsetY")
        self.visibility = layer_data.get("visible")
        self.int_grid = layer_data.get("intGridCsv")
        self.autoLayerTiles = layer_data.get("autoLayerTiles")
        self.seed = layer_data.get("seed")
        self.tilesetRelPath = layer_data.get("__tilesetRelPath")
        self.overrideTilesetUid = layer_data.get("overrideTilesetUid")
        self.tile_list = []
        for tile in layer_data.get("gridTiles"):
            self.tile_list.append(LDtkTileData(tile, self.tilesetRelPath))
        self.entity_list = []
        for entity in layer_data.get("entityInstances"):
            self.entity_list.append(LDtkEntityData(entity, self.tilesetRelPath))