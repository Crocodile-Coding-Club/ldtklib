from .tile import LDtkTileData
from .entity import LDtkEntityData

class LDtkLayerData:
    """LDtk layer data.
    
    Attributes
    ----------
    layer_unique_id : str
        The unique ID of the layer.
    tileset_relative_path : str
        Relative path of the tileset.
    level_id : int
        ID of the level.
    level_definition_id : int
        Definition ID of the level.
    visibility : bool
        Visibility status of the layer.
    x_offset : int
        X offset of the layer.
    y_offset : int
        Y offset of the layer.
    width : int
        Width of the layer in grid units.
    height : int
        Height of the layer in grid units.
    auto_layer_tiles : list
        List of auto-layer tiles.
    tile_list : list[LDtkTileData]
        List of tiles in the layer.
    entity_list : list[LDtkEntityData]
        List of entities in the layer.
    int_grid : list[int]
        List of values in the intgrid.
    seed : int
        Random seed of the layer.
    """
    def __init__(self, layer_data: dict):
        """Constructor of the LDtkLayerData class.

        Args:
            layer_data (dict): Raw JSON data of the layer.
        """
        self.layer_unique_id: str = layer_data.get("iid")

        self.tileset_relative_path: str = layer_data.get("__tilesetRelPath")

        self.level_id: int = layer_data.get("levelId")

        self.level_definition_id: int = layer_data.get("layerDefUid")

        self.visibility: bool = layer_data.get("visible")

        self.x_offset: int = layer_data.get("pxOffsetX")
        self.y_offset: int = layer_data.get("pxOffsetY")

        self.width: int = layer_data.get("__cWid")
        self.height: int = layer_data.get("__cHei")

        self.auto_layer_tiles: list = layer_data.get("autoLayerTiles")

        self.tile_list: list[LDtkTileData] = [LDtkTileData(tile, self.tileset_relative_path) for tile in layer_data.get("gridTiles")]
        self.entity_list: list[LDtkEntityData] = [LDtkEntityData(entity, self.tileset_relative_path) for entity in layer_data.get("entityInstances")]
        self.int_grid: list[int] = layer_data.get("intGridCsv")
        
        
        self.seed: int = layer_data.get("seed")

        self.raw_data = layer_data

    def getLayerUniqueID(self) -> str:
        """Get the unique ID of the layer.

        Returns:
            str: Unique ID of the layer.
        """
        return self.layer_unique_id

    def getTilesetRelativePath(self) -> str:
        """Get the relative path of the tileset.

        Returns:
            str: Relative path of the tileset.
        """
        return self.tileset_relative_path

    def getLevelID(self) -> int:
        """Get the ID of the level.

        Returns:
            int: ID of the level.
        """
        return self.level_id
    
    def getLevelDefinitionID(self) -> int:
        """Get the definition ID of the level.

        Returns:
            int: Definition ID of the level.
        """
        return self.level_definition_id

    def getVisibility(self) -> bool:
        """Get the visibility status of the layer.

        Returns:
            bool: Visibility status of the layer.
        """
        return self.visibility

    def getXOffset(self) -> int:
        """Get the X offset of the layer.

        Returns:
            int: X offset of the layer.
        """
        return self.x_offset

    def getYOffset(self) -> int:
        """Get the Y offset of the layer.

        Returns:
            int: Y offset of the layer.
        """
        return self.y_offset

    def getWidth(self) -> int:
        """Get the width of the layer in grid units.

        Returns:
            int: Width of the layer.
        """
        return self.width

    def getHeight(self) -> int:
        """Get the height of the layer in grid units.

        Returns:
            int: Height of the layer.
        """
        return self.height

    def getAutoLayerTiles(self) -> list:
        """Get the auto-layer tiles of the layer.

        Returns:
            list: Auto-layer tiles of the layer.
        """
        return self.auto_layer_tiles

    def getTileList(self) -> list[LDtkTileData]:
        """Get the list of tiles in the layer.

        Returns:
            list[LDtkTileData]: List of tiles of the layer.
        """
        return self.tile_list

    def getEntityList(self) -> list[LDtkEntityData]:
        """Get the list of entities in the layer.

        Returns:
            list[LDtkEntityData]: List of entities of the layer.
        """
        return self.entity_list

    def getIntGrid(self) -> list[int]:
        """Get the integer grid of the layer.

        Returns:
            list[int]: Integer grid of the layer.
        """
        return self.int_grid

    def getSeed(self) -> int:
        """Get the random seed of the layer.

        Returns:
            int: Seed of the layer.
        """
        return self.seed
    
    def getRawData(self) -> dict:
        """Method to get the raw data of the layer.

        Returns:
            dict: The raw data of the layer.
        """
        return self.raw_data
    
    def setVisibility(self, visibility: bool) -> None:
        """Set the visibility of the layer.

        Args:
            visibility (bool): New visibility status of the layer.
        """
        self.visibility = visibility

    def setTileList(self, tile_list: list[LDtkTileData]) -> None:
        """Set the list of tiles in the layer.

        Args:
            tile_list (list[LDtkTileData]): New list of tiles.
        """
        self.tile_list = tile_list

    def setEntityList(self, entity_list: list[LDtkEntityData]) -> None:
        """Set the list of entities in the layer.

        Args:
            entity_list (list[LDtkEntityData]): New list of entities.
        """
        self.entity_list = entity_list

    def setIntGrid(self, int_grid: list[int]) -> None:
        """Set the integer grid of the layer.

        Args:
            int_grid (list[int]): New integer grid values.
        """
        self.int_grid = int_grid