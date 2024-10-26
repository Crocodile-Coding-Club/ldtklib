class LDtkEntityData:
    """LDtk entity data.
    
    Attributes
    ----------
    entity_unique_id : str
        The unique id of the entity.
    tileset_relative_path : str | None
        Relative path of the tileset.
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
    """
    def __init__(self, entity_data: dict, tileset_relative_path: str | None = None):
        """Constructor of the LDtkEntityData class.

        Args:
            entity_data (dict): Raw JSON data of the entity.
            tileset_relative_path (str | None): Relative path of the tileset.
        """
        self.entity_unique_id = entity_data.get("iid")

        self.entity_definiton_id = entity_data.get("defUid")

        self.field_list = entity_data.get("fieldInstances")

        self.x: int = entity_data.get("px")[0]
        self.y: int = entity_data.get("px")[1]

        self.height = entity_data.get("height")
        self.width = entity_data.get("width")

        self.source_x = entity_data.get("__tile").get("x")
        self.source_y = entity_data.get("__tile").get("y")