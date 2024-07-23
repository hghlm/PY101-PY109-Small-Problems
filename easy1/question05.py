bill = float(input('What is the bill? '))
tip_rate = float(input('What is the tip percentage? '))

tip = bill * tip_rate/100
total = "{:.2f}".format(bill + tip)

print(f'The tip is ${"{:.2f}".format(tip)}.')
print(f'The total is ${total}. ')
