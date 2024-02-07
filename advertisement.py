from estate import Apartment, House, Shop
from deal import Sell, Rent


class ApartmentSell(Apartment, Sell):
    
    def show_detail(self):
        self.show_description()
        self.show_price()

class ApartmentRent(Apartment, Rent):
    pass


class HouseSell(House, Sell):
    pass


class HouseRent(House, Rent):
    pass


class ShopSell(Shop, Sell):
    pass


class ShopRent(Shop, Rent):
    pass