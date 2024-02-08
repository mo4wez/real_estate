from abc import ABC


class Sell(ABC):
    def __init__(self, price_per_meter: float, discountable: bool, convertible: bool, *args, **kwargs):
        self.price_per_meter = price_per_meter
        self.discountable = discountable
        self.convertible = convertible
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f'Price: {self.price_per_meter}\t Discount: {self.discountable}\t Convrtible: {self.convertible}')


class Rent(ABC):
    def __init__(self, initial_price: float, monthly_price: float, discountable: bool, convertible: bool, *args, **kwargs):
        self.initial_price = initial_price
        self.monthly_price = monthly_price
        self.discountable = discountable
        self.convertible = convertible
        super().__init__(*args, **kwargs)

    def show_price(self):
        print(f'Monthly Price: {self.monthly_price}\t Discount: {self.discountable}\t Convrtible: {self.convertible}')