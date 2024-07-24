def oddities(list_):
    ans = []
    
    for i in range(0, len(list_), 2):
        ans.append(list_[i])
        
    return ans
    # return list_[::2]
    
def evenies(list_):
    return list_[1::2]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

print(evenies([2, 3, 4, 5, 6]) == [3, 5])  # True
