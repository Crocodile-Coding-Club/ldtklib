class LDtkTileData:
    """
    A class to represent a person.

    Attributes
    ----------
    tile_id : int
        The id of the tile in the tileset
    opacity : int
        Opacity of the tile. Goes from 0 to 1.
    flip_bits: int
        A 2-bits integer to represent the mirror transformations of the tile.
        f=0 (no flip), f=1 (X flip only), f=2 (Y flip only), f=3 (both flips)
    x : int
        The x position of the tile on the layer.
    y : int
        The y position of the tile on the layer.
    width : int
        The width of the tile.
    height : int
        The height of the tile.
    source_x : int
        The x position of the tile on the tileset.
    source_y : int
        The y position of the tile on the tileset.
    """

    def __init__(self, tile_data:dict):
        """Constructor of the TileData class

        Args:
            tile_data (dict): Raw JSON data of the tile
        """
        self.tile_id: int = tile_data.get("t")

        self.opacity: int = tile_data.get("a")

        self.flip_bits: int = tile_data.get("f")

        self.x: int = tile_data.get("px")[0]
        self.y: int = tile_data.get("px")[1]

        self.width = tile_data.get("__cWid")
        self.height = tile_data.get("__cHei")


        self.source_x: int = tile_data.get("src")[0]
        self.source_y: int = tile_data.get("src")[1]


    def getTileId(self) -> int:
        """Method to get the id of the tile.

        Returns:
            int: Id of the tile.
        """
        return self.tile_id
    
    def getX(self) -> int:
        """Method to get the x position of the tile on the layer.

        Returns:
            int: X position of the tile on the layer.
        """
        return self.x
    
    def getWidth(self) -> int:
        """Method to get the width of the tile.

        Returns:
            int: Width of the tile.
        """
        return self.width
    
    def getHeight(self) -> int:
        """Method to get the height of the tile.

        Returns:
            int: Height of the tile.
        """
        return self.height
    
    def getY(self) -> int:
        """Method to get the y position of the tile on the layer.

        Returns:
            int: Y position of the tile on the layer.
        """
        return self.y
    
    def getOpacity(self) -> int:
        """Method to get the opacity of the tile on the layer.

        Returns:
            int: Opacity of the tile on the layer.
        """
        return self.opacity
    
    def getFlipbits(self) -> int:
        """Method to get the flipbits of the tile.

        Flipbits are 2-bits integer to represent the mirror transformations of the tile.
        f=0 (no flip), f=1 (X flip only), f=2 (Y flip only), f=3 (both flips)

        Returns:
            int: Flipbits of the tile on the layer.
        """
        return self.flip_bits
    
    def getSourceX(self) -> int:
        """Method to get the x position of the tile on the tileset

        Returns:
            int: X position of the tile on the tileset
        """
        return self.source_x
    
    def getSourceY(self) -> int:
        """Method to get the y position of the tile on the tileset

        Returns:
            int: Y position of the tile on the tileset
        """
        return self.source_y
    