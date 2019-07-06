str1 = input()
str2 = input()
output = ''
for char in str1:
    if char in str2 and char not in output:
        output += char
print(output)
