letters = input("INPUT:")
output = ''
for char in letters:
    if char.isupper() is True:
        output += chr(64 + ((ord(char)-63) % 26))
    elif char.islower() is True:
        output += chr(96 + ((ord(char)-95) % 26))
print(output)
