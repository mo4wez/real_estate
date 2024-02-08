from base import BaseClass
from estate import Apartment, House, Shop
from deal import Sell, Rent


class ApartmentSell(BaseClass, Apartment, Sell):
    
    def show_detail(self):
        self.show_description()
        self.show_price()

class ApartmentRent(BaseClass, Apartment, Rent):

    def show_detail(self):
        self.show_description()
        self.show_price()


class HouseSell(BaseClass, House, Sell):

    def show_detail(self):
        self.show_description()
        self.show_price()


class HouseRent(BaseClass, House, Rent):
    def show_detail(self):
        self.show_description()
        self.show_price()



class ShopSell(BaseClass, Shop, Sell):
    pass


class ShopRent(Shop, Rent):
    pass