array = input().split(' ')
output = ''
if len(array[-1]) == 1:
    for char in array[-2]:
        if char.isalpha() is True:
            output += char
    
else:
    for char in array[-1]:
        if char.isalpha() is True:
            output += char
print(output)
    
