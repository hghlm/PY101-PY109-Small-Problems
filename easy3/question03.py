def print_in_box(string):
    border = '-' * (len(string) + 2)
    space = ' ' * (len(string) + 2)
    
    print(f'+{border}+')
    print(f'|{space}|')
    print(f'| {string} |')
    print(f'|{space}|')
    print(f'+{border}+')

print_in_box('To boldly go where no one has gone before.')
print_in_box('')
