number = int(input('Please enter an integer greater than 0: '))
sum_or_product = input(f'Enter "s" to compute the sum, or "p" to compute the product. ')
print()

if sum_or_product == 's':
    sum_answer = 0
    
    for x in range(1, number + 1):
        sum_answer += x
    
    print(f'The sum of the integers between 1 and {number} is {sum_answer}.')

elif sum_or_product == 'p':
    product = 1
    
    for x in range(1, number + 1):
        product *= x
    
    print(f'The product of the integers between 1 and {number} is {product}.')
    
else:
    print('Error.')