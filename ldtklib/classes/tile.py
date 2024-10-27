class LDtkTileData:
    """LDtk tile data.

    Attributes
    ----------
    tile_id : int
        The id of the tile.
    tileset_relative_path : str | None
        Relative path of the tileset.
    opacity : float
        Opacity of the tile. Goes from 0 to 1.
    x : int
        The x position of the tile.
    y : int
        The y position of the tile.
    width : int
        The width of the tile.
    height : int
        The height of the tile.
    flipbits : int
        A 2-bits integer to represent the mirror transformations of the tile.
        f=0 (no flip), f=1 (X flip only), f=2 (Y flip only), f=3 (both flips)
    source_x : int
        The x position of the tile on the tileset.
    source_y : int
        The y position of the tile on the tileset.
    raw_data : dict
        The raw data of the tile.
    """

    def __init__(self, tile_data: dict, tileset_relative_path: str | None = None):
        """Constructor of the LDtkTileData class

        Args:
            tile_data (dict): Raw JSON data of the tile.
            tileset_relative_path (str | None): Relative path of the tileset.
        """
        self.tile_id: int = tile_data.get("t")

        self.tileset_relative_path: str = tileset_relative_path

        self.opacity: float = tile_data.get("a")

        self.x: int = tile_data.get("px")[0]
        self.y: int = tile_data.get("px")[1]

        self.width = tile_data.get("__cWid")
        self.height = tile_data.get("__cHei")

        self.flipbits: int = tile_data.get("f")

        self.source_x: int = tile_data.get("src")[0]
        self.source_y: int = tile_data.get("src")[1]

        self.raw_data = tile_data

    def getTileId(self) -> int:
        """Method to get the id of the tile.

        Returns:
            int: Id of the tile.
        """
        return self.tile_id
    
    def getTilesetRelativePath(self) -> str | None:
        """Method to get the relative path of the tileset.

        Returns:
            str | None: The relative path of the tileset, if available.
        """
        return self.tileset_relative_path
    
    def getOpacity(self) -> int:
        """Method to get the opacity of the tile.

        Returns:
            int: Opacity of the tile.
        """
        return self.opacity
    
    def getX(self) -> int:
        """Method to get the x position of the tile.

        Returns:
            int: The x position of the tile.
        """
        return self.x
    
    def getY(self) -> int:
        """Method to get the y position of the tile.

        Returns:
            int: The y position of the tile.
        """
        return self.y
    
    def getWidth(self) -> int:
        """Method to get the width of the tile.

        Returns:
            int: The width of the tile.
        """
        return self.width
    
    def getHeight(self) -> int:
        """Method to get the height of the tile.

        Returns:
            int: The height of the tile.
        """
        return self.height
    
    def getFlipbits(self) -> int:
        """Method to get the flipbits of the tile.

        Flipbits are 2-bits integer to represent the mirror transformations of the tile.
        f=0 (no flip), f=1 (X flip only), f=2 (Y flip only), f=3 (both flips)

        Returns:
            int: Flipbits of the tile.
        """
        return self.flipbits
    
    def getSourceX(self) -> int:
        """Method to get the x position of the tile on the tileset

        Returns:
            int: The x position of the tile on the tileset.
        """
        return self.source_x
    
    def getSourceY(self) -> int:
        """Method to get the y position of the tile on the tileset

        Returns:
            int: The y position of the tile on the tileset.
        """
        return self.source_y
    
    def getRawData(self) -> dict:
        """Method to get the raw data of the tile.

        Returns:
            dict: The raw data of the tile.
        """
        return self.raw_data
    
    def setOpacity(self, opacity: float) -> None:
        """Method to set the opacity of the tile.

        Args:
            opacity (float): New opacity of the tile.
        """
        self.opacity = opacity
    
    def setX(self, x: int) -> None:
        """Method to set the x position of the tile.

        Args:
            x (int): New x position of the tile.
        """
        self.x = x
    
    def setY(self, y: int) -> None:
        """Method to set the y position of the tile.

        Args:
            y (int): New y position of the tile.
        """
        self.y = y
    
    def setWidth(self, width: int) -> None:
        """Method to set the width position of the tile.

        Args:
            width (int): New width of the tile.
        """
        self.width = width
    
    def setHeight(self, height: int) -> None:
        """Method to set the height position of the tile.

        Args:
            height (int): New height of the tile.
        """
        self.height = height
    
    def setFlipbits(self, flipbits: int) -> None:
        """Method to set the flipbits of the tile.

        Args:
            flipbits (int): New flipbits of the tile.
        """
        self.flipbits = flipbits