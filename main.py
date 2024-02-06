from user import User
from random import choice

FIRST_NAME = ['moawezz', 'yasin', 'naseer', 'amir']
LAST_NAME = ['deh', 'sbz', 'rah', 'naderi']
MOBILES = ['5878', '3462', '2935', '2310', '6745', '2245']

if __name__ == '__main__':
    for mobile in MOBILES:
        User(choice(FIRST_NAME), choice(LAST_NAME), mobile)

    for user in User.objects_list:
        print(user.id, '-', user.fullname)