class LDtkEntityData:
    """LDtk entity data.
    
    Attributes
    ----------
    entity_unique_id : str
        The unique id of the entity.
    tileset_relative_path : str | None
        Relative path of the tileset.
    entity_definiton_id : int
        Definition id of the entity.
    field_list : list
        List of all custom fields of the entity.
    x : int
        The x position of the entity.
    y : int
        The y position of the entity.
    width : int
        The width of the entity.
    height : int
        The height of the entity.
    source_x : int
        The x position of the entity on the tileset.
    source_y : int
        The y position of the entity on the tileset.
    raw_data : dict
        The raw data of the entity.
    """
    def __init__(self, entity_data: dict, tileset_relative_path: str | None = None):
        """Constructor of the LDtkEntityData class.

        Args:
            entity_data (dict): Raw JSON data of the entity.
            tileset_relative_path (str | None): Relative path of the tileset.
        """
        self.entity_unique_id: str = entity_data.get("iid")

        self.tileset_relative_path: str | None = tileset_relative_path

        self.entity_definiton_id: int = entity_data.get("defUid")

        self.field_list: list = entity_data.get("fieldInstances")

        self.x: int = entity_data.get("px")[0]
        self.y: int = entity_data.get("px")[1]

        self.height: int = entity_data.get("height")
        self.width: int = entity_data.get("width")

        self.source_x: int = entity_data.get("__tile").get("x")
        self.source_y: int = entity_data.get("__tile").get("y")

        self.raw_data = entity_data
    
    def getUniqueID(self) -> str:
        """Method to get the unique id of the entity.

        Returns:
            str: Unique id of the tile.
        """
        return self.entity_unique_id

    def getTilesetRelativePath(self) -> str | None:
        """Method to get the relative path of the tileset.

        Returns:
            str | None: The relative path of the tileset, if available.
        """
        return self.tileset_relative_path
    
    def getDefinitionID(self) -> int:
        """Method to get the definition id of the entity.

        Returns:
            int: Definition id of the entity.
        """
        return self.entity_definiton_id
    
    def getFieldList(self) -> list:
        """Method to get the field list of the entity.

        Returns:
            int: Field list of the entity.
        """
        return self.field_list

    def getX(self) -> int:
        """Method to get the x position of the entity.

        Returns:
            int: The x position of the entity.
        """
        return self.x

    def getY(self) -> int:
        """Method to get the y position of the entity.

        Returns:
            int: The y position of the entity.
        """
        return self.y

    def getWidth(self) -> int:
        """Method to get the width of the entity.

        Returns:
            int: The width of the entity.
        """
        return self.width

    def getHeight(self) -> int:
        """Method to get the height of the entity.

        Returns:
            int: The height of the entity.
        """
        return self.height


    def getSourceX(self) -> int:
        """Method to get the x position of the entity on the tileset.

        Returns:
            int: The x position of the entity on the tileset.
        """
        return self.source_x

    def getSourceY(self) -> int:
        """Method to get the y position of the entity on the tileset.

        Returns:
            int: The y position of the entity on the tileset.
        """
        return self.source_y

    def getRawData(self) -> dict:
        """Method to get the raw data of the entity.

        Returns:
            dict: The raw data of the entity.
        """
        return self.raw_data
    
    def setX(self, x: int) -> None:
        """Method to set the x position of the entity.

        Args:
            x (int): New x position of the entity.
        """
        self.x = x

    def setY(self, y: int) -> None:
        """Method to set the y position of the entity.

        Args:
            y (int): New y position of the entity.
        """
        self.y = y

    def setWidth(self, width: int) -> None:
        """Method to set the width of the entity.

        Args:
            width (int): New width of the entity.
        """
        self.width = width

    def setHeight(self, height: int) -> None:
        """Method to set the height of the entity.

        Args:
            height (int): New height of the entity.
        """
        self.height = height