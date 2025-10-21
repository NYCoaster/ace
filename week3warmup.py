favorite_number = input('What is your favorite number?')
favorite_number = int (favorite_number)

if favorite_number <= 10 :
    print ('Your number is between 1-10')
else:
    print('Your number is greater than 10')

favorite_food = input('What is your favorite food out of these, Yougurt, Icecream, or Chicken')

if favorite_food == 'Yougurt' or 'Icecream':
    print ('You like my top 2 favorite food')
else:
    print ('I hate chicken')

place = input('Where do you want to go: Home, Work, Resterant, Club')

if place == 'Home':
    thing = input('You are at home, what do you want to do?')
    print (f'You are {thing}')

if place == 'Work':
    thing = input('You are at work, what do you want to do?')
    print (f'You are {thing}')

if place == 'Resterant':
    thing = input('You are at a Resterant, what do you want to order?')
    print (f'You ordered {thing}')

if place == 'Club':
    thing = input('You are at a club, who do you want to dance with?')
    print (f'You are dancing with {thing}')