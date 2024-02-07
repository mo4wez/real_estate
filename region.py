from base import BaseClass


class Region(BaseClass):
    
    def __init__(self, name: str, *args, **kwargs):
        self.name = name
        super().__init__(*args, *kwargs)