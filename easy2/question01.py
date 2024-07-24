def greetings(l, d):
    ans = 'Hello, '
    
    for word in l:
        ans += word
        if word != l[len(l)-1]:
            ans += ' '
    
    ans += f'! Nice to have a {d["title"]} {d["occupation"]} around.'
        
    return ans
    

greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

