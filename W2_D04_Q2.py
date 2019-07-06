word = list(input("WORD?"))
N = int(input("N?"))
output1 = ''
for char in word:
    output1 += chr(64 +(ord(char) + N -64 ) % 26)
output2 = list(output1)
for i in range(len(word)):
    output2[(i + N) % len(word)] = output1[i]
output = ''
for j in output2:
    output += j
print(output)
    
