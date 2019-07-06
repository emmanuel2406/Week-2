array = input("Input:").split(' ')
datalist = []

for word in array:
    count = 0
    for char in word:
        if char.isalpha() is True:
            count += 1
    datalist.append(count)
n = 0
for item in datalist:
    n += item
n = n / len(datalist)
print(round(n,2))
