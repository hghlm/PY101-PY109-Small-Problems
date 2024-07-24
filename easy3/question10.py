def century(year):
    cent = int(year / 100)
    
    if year % 100 != 0:
        cent += 1
    
    if cent % 10 == 1 and cent % 100 != 11:
        return f'{cent}st'
    elif cent % 10 == 2 and cent % 100 != 12:
        return f'{cent}nd'
    elif cent % 10 == 3 and cent % 100 != 13:
        return f'{cent}rd'
    else:
        return f'{cent}th'
   
    
        

print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True