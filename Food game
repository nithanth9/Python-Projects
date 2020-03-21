global score

name = [
    'fillet', 'null', 'null', 'gumbo', 'tuna salad', 'fish sandwich', 'sushi', 'fish and chips', 'grilled fish', 'null',
    'spagety meetballs', 'roast beef',  'null', 'beef stew', 'beef thai salad', 'hamburger', 'beef burrito', 'steak', 'null', 'cheeseburger',
    'pancake', 'null', 'baguette', 'ramen noodles', 'mac and cheese', 'empty sandwich', 'null', 'doughnut', 'null', 'grilled cheese',  
    'porkchops', 'pork roast', 'baked ham', 'null', 'null', 'null', 'ham cheese sandwich', 'null', 'barbeque grilled ribs', 'null',
    'chicken alfredo', 'rotisserie', 'null', 'chicken noodle soup', 'chicken salad', 'chicken sandwich', 'chicken wrap', 'null', 'fried chicken', 'teriyaki chicken', 
    'eggplant fried in a pan', 'null', 'null', 'eggplant soup', 'eggplant salad', 'null', 'eggplant wrap', 'eggplant fries', 'grilled eggplant', 'null',
    'hashbrown', 'whole roasted potato', 'baked potato', 'mashed potato', 'potato salad', 'null', 'null', 'friend fries', 'null', 'null',
    'null', 'coffee', 'baked beans', 'boiled peas', 'tofu salad', 'null', 'bean burrito', 'soylent green', 'null', 'null'
    ]
    # 15, 24
ing1 = ['fish', 'beef', 'dough', 'pork', 'chicken', 'eggplant', 'potato', 'bean']
ing2 = ['none', 'pasta/noodles', 'cheese']
cook = ['pan', 'roast', 'bake', 'boil', 'salad', 'sandwich', 'wrap', 'deep fry', 'grill']
def smalline():
    print('-'*75)

def line():
    print('='*75)
    print(' ')

def order():
    dish = 0
    from random import randint
    dish = randint(0 , 9) + 10*randint(0 , 7)
   
    while name[int(dish)] == 'null':
        dish = randint(0 , 9) + 10*randint(0 , 7)
    print('ORDER: %r' % name[int(dish)])
    smalline()   
    main = input('''
CHOOSE YOUR MAIN INGREDIENT:
   
    1.)fish     2.)beef     3.)dough     4.)pork    
    5.)chicken     6.)eggplant     7.)potato     8.) beans
   
''')
    main = int(main) - 1
    smalline()
    print("INGREDIENT 1: %s" % (ing1[main]))
    smalline()
    side = input('''
CHOOSE YOUR SECOND INGREDIENT:

    1.)none     2.)pasta/noodles (not with other pasta)     3.)cheese
''')
    side = int(side) - 1
    smalline()
    print('INGREDIENT 2: %s' % (ing2[side]))
    smalline()
    prep = input('''
PERPARATION:

    1.)pan     2.)roast     3.)bake     4.)boil     5.)salad
    6.)sandwich     7.)wrap     8.)deep fry     9.)grill
''')
    prep = int(prep) - 1
    smalline()
    print('INGREDIENT 2: %s' % (cook[prep]))
    smalline()
   
    chef = main*10 + prep
    if chef == 15 and side == 2:
        chef = chef + 4
    elif chef == 24 and side == 2:
        chef = chef + 1
    print('you made %r' % name[int(chef)])
    if chef == dish:
        print('NICE JOB')
        smalline()
        order()
    else:
        print('YOU FAILED')
        smalline()
        order()
       
   
   
   
   
   
line()



print('''
        WELCOME TO THE FOOD HOUSE
       
        ARE YOU READY TO COOK?
    ''')
line()
start = raw_input('Y/N')
if start == 'Y':
    print('Let\'s go!')
    order()
else:
    print('Well get ready!')
    line()
    line()
    order()
