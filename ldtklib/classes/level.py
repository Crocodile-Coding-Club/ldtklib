from .layer import LDtkLayerData

class LDtkLevelData:
    """LDtk level data.

    Attributes
    ----------
    identifier : str
        The identifier of the level.
    level_unique_id : str
        The unique ID of the level.
    background_relative_path : str | None
        The relative path to the background, if available.
    external_relative_path : str | None
        The relative path to external level data, if available.
    field_instances : list
        List of field instances within the level.
    neighbours : list
        List of neighbouring levels.
    background_color : str
        The background color of the level.
    background_position : str
        The position of the background image.
    depth : int
        The depth of the level in the world.
    x : int
        The x position of the level in the world.
    y : int
        The y position of the level in the world.
    width : int
        The width of the level in pixels.
    height : int
        The height of the level in pixels.
    layerInstances : list[LDtkLayerData]
        List of layer instances in the level.
    """

    def __init__(self, level_data: dict):
        self.identifier: str = level_data.get("identifier")
        self.level_unique_id: str = level_data.get("iid")

        self.background_relative_path: str | None = level_data.get("bgRelPath")
        self.external_relative_path: str | None = level_data.get("externalRelPath")

        self.field_instances: list = level_data.get("fieldInstances")

        self.neighbours: list = level_data.get("__neighbours")

        self.background_color: str = level_data.get("__bgColor")
        self.background_position: str = level_data.get("__bgPos")

        self.depth: int = level_data.get("worldDepth")

        self.x: int = level_data.get("worldX")
        self.y: int = level_data.get("worldY")

        self.width: int = level_data.get("pxWid")
        self.height: int = level_data("pxHei")

        self.layerInstances: list[LDtkLayerData] = [LDtkLayerData(layer) for layer in level_data.get("layerInstances", [])]

        self.raw_data = level_data
    
    def getIdentifier(self) -> str:
        """Get the identifier of the level.

        Returns:
            str: The identifier of the level.
        """
        return self.identifier

    def getLevelUniqueID(self) -> str:
        """Get the unique ID of the level.

        Returns:
            str: The unique ID of the level.
        """
        return self.level_unique_id

    def getBackgroundRelativePath(self) -> str | None:
        """Get the relative path to the background, if available.

        Returns:
            str | None: The relative path to the background.
        """
        return self.background_relative_path

    def getExternalRelativePath(self) -> str | None:
        """Get the relative path to external level data, if available.

        Returns:
            str | None: The relative path to external data.
        """
        return self.external_relative_path

    def getFieldInstances(self) -> list:
        """Get the field instances within the level.

        Returns:
            list: List of field instances.
        """
        return self.field_instances

    def getNeighbours(self) -> list:
        """Get the neighbouring levels.

        Returns:
            list: List of neighbours.
        """
        return self.neighbours

    def getBackgroundColor(self) -> str:
        """Get the background color of the level.

        Returns:
            str: The background color.
        """
        return self.background_color

    def getBackgroundPosition(self) -> str:
        """Get the position of the background image.

        Returns:
            str: The background position.
        """
        return self.background_position

    def getDepth(self) -> int:
        """Get the depth of the level in the world.

        Returns:
            int: The depth of the level.
        """
        return self.depth

    def getX(self) -> int:
        """Get the x position of the level in the world.

        Returns:
            int: The x position of the level.
        """
        return self.x

    def getY(self) -> int:
        """Get the y position of the level in the world.

        Returns:
            int: The y position of the level.
        """
        return self.y

    def getWidth(self) -> int:
        """Get the width of the level in pixels.

        Returns:
            int: The width of the level.
        """
        return self.width

    def getHeight(self) -> int:
        """Get the height of the level in pixels.

        Returns:
            int: The height of the level.
        """
        return self.height

    def getLayerInstances(self) -> list[LDtkLayerData]:
        """Get the list of layer instances in the level.

        Returns:
            list[LDtkLayerData]: List of layer instances.
        """
        return self.layerInstances
    
    def getRawData(self) -> dict:
        """Method to get the raw data of the level.

        Returns:
            dict: The raw data of the level.
        """
        return self.raw_data
