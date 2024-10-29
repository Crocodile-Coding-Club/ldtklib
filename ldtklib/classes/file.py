import json
from .world import LDtkWorldData

class LDtkFile:
    """LDtk file data loader.

    Attributes
    ----------
    world_data : LDtkWorldData
        The world data contained in the file.
    """
    def __init__(self, file_relative_path):
        """Constructor for the LDtkFile class.

        Args:
            file_relative_path (str): The relative path to the LDtk JSON file.
        """
        with open(file_relative_path, 'r') as file:
            data = json.load(file)
        self.world_data = LDtkWorldData(data)
    
    def getWorldData(self) -> LDtkWorldData:
        """Get the world data from the file.

        Returns:
            LDtkWorldData: The world data contained in the file.
        """
        return self.world_data