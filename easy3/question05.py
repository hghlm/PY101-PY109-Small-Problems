def triangle(num):
    for i in range(1,num+1):
        print(f'{" " * (num - i)}{"*" * (i)}')

triangle(5)
triangle(9)
    