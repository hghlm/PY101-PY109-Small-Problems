def short_long_short(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a


# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")