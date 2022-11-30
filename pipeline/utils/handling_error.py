class TranformsErrorType(Exception):
    def __init__(self, transforms):
        self.transforms = transforms
        self.details = f"Transform must be a Dict, but {self.transforms} is {type(self.transforms)}!!!"
        super().__init__(self.details)


class KeyTransformsNotInDataset(Exception):
    def __init__(self, key):
        self.key = key
        self.details = f"{self.key} not in Dataset"
        super().__init__(self.details)
