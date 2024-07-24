def penultimate(string):
    words = string.split(' ')
    
    return words[-2]
    
def middle(string):
    words = string.split(' ')
    
    if len(words) % 2 == 0:
        return("No middle word.")
    elif len(words) == 0:
        return("No words.")
    else:
        return words[len(words)//2]
    
# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")

print(middle("Print the middle."))
print(middle("One."))
print(middle("This will not work."))


