class LDtkEntityData:
    def __init__(self, entity_data: dict):
        self.entity_id = entity_data.get("iid")
        self.defUid = entity_data.get("defUid")
        self.fieldInstances = entity_data.get("fieldInstances")
        self.height = entity_data.get("height")
        self.width = entity_data.get("width")
        self.x: int = entity_data.get("px")[0]
        self.y: int = entity_data.get("px")[1]
        self.source_x = entity_data.get("__tile").get("x")
        self.source_y = entity_data.get("__tile").get("y")
        pass