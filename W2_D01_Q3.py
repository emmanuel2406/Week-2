str1 = input()
str2 = input()
output = ''
for char in str1:
    if char not in output:
        output += char
for char in str2:
    if char not in output:
        output += char


print(output)
