from .level import LDtkLevelData

class LDtkWorldData:
    """LDtk world data.

    Attributes
    ----------
    identifier : str
        The identifier of the world.
    world_unique_id : str
        The unique ID of the world.
    levels : list[LDtkLevelData]
        List of levels in the world.
    width : int
        Width of the world grid in units.
    height : int
        Height of the world grid in units.
    layout : str
        Layout type of the world.
    """
    def __init__(self, world_data:dict):
        """Constructor for the LDtkWorldData class.

        Args:
            world_data (dict): Raw JSON data of the world.
        """
        self.identifier: str = world_data.get("identifier")

        self.world_unique_id: str = world_data.get("iid")

        self.levels: list[LDtkLevelData] = [LDtkLevelData(level) for level in world_data.get("levels", [])]

        self.width: int = world_data.get("worldGridWidth")
        self.height: int = world_data.get("worldGridHeight")

        self.layout: str = world_data.get("worldLayout")

        self.raw_data = world_data

    def getIdentifier(self) -> str:
        """Get the identifier of the world.

        Returns:
            str: The identifier of the world.
        """
        return self.identifier

    def getWorldUniqueID(self) -> str:
        """Get the unique ID of the world.

        Returns:
            str: The unique ID of the world.
        """
        return self.world_unique_id

    def getLevels(self) -> list[LDtkLevelData]:
        """Get the list of levels in the world.

        Returns:
            list[LDtkLevelData]: List of levels in the world.
        """
        return self.levels

    def getWidth(self) -> int:
        """Get the width of the world grid in units.

        Returns:
            int: Width of the world grid.
        """
        return self.width

    def getHeight(self) -> int:
        """Get the height of the world grid in units.

        Returns:
            int: Height of the world grid.
        """
        return self.height

    def getLayout(self) -> str:
        """Get the layout type of the world.

        Returns:
            str: Layout type of the world.
        """
        return self.layout
    
    def getRawData(self) -> dict:
        """Method to get the raw data of the world.

        Returns:
            dict: The raw data of the world.
        """
        return self.raw_data