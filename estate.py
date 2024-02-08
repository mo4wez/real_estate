from abc import ABC, abstractmethod


class EstateAbstract(ABC):
    def __init__(self, user, area: float, rooms_count: int, built_year: int, region, address: str, *args, **kwargs):
        self.user = user
        self.area = area
        self.rooms_count = rooms_count
        self.built_year = built_year
        self.region = region
        self.address = address
        super().__init__(*args, **kwargs)

    @abstractmethod
    def show_description(self):
        pass
        

class Apartment(EstateAbstract):
    def __init__(self, has_elevator: bool, has_parking: bool, floor: int, *args, **kwargs):
        self.has_elevator = has_elevator
        self.has_parking = has_parking
        self.floor = floor
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f'Apartment {self.id}\t area: {self.area}\t address: {self.address}')


class House(EstateAbstract):
    def __init__(self, has_yard: bool, floors_count: int, *args, **kwargs):
        self.has_yard = has_yard
        self.floors_count = floors_count
        super().__init__(*args, **kwargs)

    def show_description(self):
        print(f'House {self.id}\t area: {self.area}\t address: {self.address}')


class Shop(EstateAbstract):
    
    def show_description(self):
        print(f'Shop {self.id}')