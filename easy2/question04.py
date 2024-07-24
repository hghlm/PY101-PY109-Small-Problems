def multiply(x, y):
    return x * y

def square(x):
    return multiply(x, x)
    
def power(x, exp):
    ans = x
    
    while exp > 1:
        ans = multiply(x, ans)
        exp -= 1
    
    return ans
        
    
print(square(5) == 25)   # True
print(square(-8) == 64)  # True

print(power(5, 2))
print(power(2, 3))