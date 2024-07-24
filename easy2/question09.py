import random

name = input('Enter name: ')

if name == "":
    print(f'Teddy is {random.randrange(20, 100, 1)} years old!')
else:
    print(f'{name} is {random.randrange(20, 100, 1)} years old!')