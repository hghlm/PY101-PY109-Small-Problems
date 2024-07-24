def xor(a, b):
    if a and b:
        return False
    elif a or b:
        return True
    else:
        return False

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)