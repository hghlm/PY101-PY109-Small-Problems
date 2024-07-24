def stringy(num):
    counter = 0
    ans = ''
    
    while counter < num:
        if counter % 2 == 0:
            ans += '1'
        else:
            ans += '0'
        counter += 1
    
    return ans
        

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True