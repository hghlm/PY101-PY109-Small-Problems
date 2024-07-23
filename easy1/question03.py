starting_range = int(input('Enter starting range: '))
ending_range = int(input('Enter ending range: '))

if starting_range % 2 != 0:
    starting_range += 1

for x in range(starting_range, ending_range + 1, 2):
    print(x)