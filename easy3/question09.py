def clean_up(string):
    ans = ''
    
    for char in string:
        if (ord(char) >= ord('a') and ord(char) <= ord('z')) or (ord(char) >= ord('A') and ord(char) <= ord('Z')):
            ans += char
        else:
            if not ans.endswith(' '):
                ans += ' '
    
    return ans

print(clean_up("---what's my +*& line?") == " what s my line ")
# True