from user import User
from estate import Apartment, House, Shop
from region import Region
from advertisement import ApartmentRent, ApartmentSell, HouseRent, HouseSell
from random import choice


FIRST_NAME = ['moawezz', 'yasin', 'naseer', 'amir']
LAST_NAME = ['deh', 'sbz', 'rah', 'naderi']
MOBILES = ['5878', '3462', '2935', '2310', '6745', '2245']

if __name__ == '__main__':
    for mobile in MOBILES:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    # for user in User.objects_list:
    #     print(user.id, '-', user.fullname)

    reg_1 = Region(name='Golshahr')

    apt_1 = Apartment(
        user=User.objects_list[0],
        area=102.3,
        rooms_count=8,
        built_year=1383,
        region=reg_1,
        address='Chabahar',
        has_elevator=True,
        has_parking=False,
        floor=4,
    )

    # apt_1.show_description()

    reg_2 = Region(name='Zibashahr')

    h_1 = House(
        user=User.objects_list[1],
        area=203.3,
        rooms_count=4,
        built_year=1401,
        region=reg_2,
        address='Zahedan',
        has_yard=True,
        floors_count=2,
    )

    # h_1.show_description()

    reg_3 = Region(name='Koy-e-Bandar')
    sp_1 = Shop(
        user=User.objects_list[2],
        area=300,
        rooms_count=2,
        built_year=1397,
        region=reg_3,
        address='Nikshahr',
    )

    # sp_1.show_description()

    apartment_sell = ApartmentSell(
        user=User.objects_list[3],
        area=213.3,
        rooms_count=8,
        built_year=1383,
        region=reg_1,
        address='Chabahar',
        has_elevator=False,
        has_parking=True,
        floor=1,
        price_per_meter=3000,
        discountable=True,
        convertible=False
    )

    apartment_sell.show_detail()

    apartment_rent = ApartmentRent(
        user=User.objects_list[0],
        area=94.3,
        rooms_count=3,
        built_year=1378,
        region=reg_1,
        address='Qasr-e-Qand',
        initial_price=230,
        monthly_price=13,
        discountable=False,
        convertible=False,
        has_elevator=False,
        has_parking=True,
        floor=0
    )

    apartment_rent.show_detail()

    house_rent = HouseRent(
        user=User.objects_list[1],
        area=23.2,
        rooms_count=1,
        built_year=1399,
        region=reg_1,
        address='Tehran',
        has_yard=False,
        floors_count=1,
        monthly_price=310,
        initial_price=15,
        discountable=False,
        convertible=True      
    )

    house_rent.show_detail()

    house_sell = HouseSell(
        user=User.objects_list[4],
        area=130.2,
        rooms_count=4,
        built_year=1400,
        region=reg_1,
        address='Kerman',
        has_yard=True,
        floors_count=1,
        price_per_meter=1300,
        discountable=True,
        convertible=True
    )

    house_sell.show_detail()

    search_result = ApartmentSell.manager.search(region=reg_1)

    print(search_result)

    res = HouseSell.manager.get(address='3')
    
    print(res)