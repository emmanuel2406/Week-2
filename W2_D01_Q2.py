array = input("Start with:").split(' ')
N = int(input("N:"))
a = int(array[0])
b = int(array[1])
c = int(array[2])
count = 3
while count != N:
    c = a + b + c
    b = c -a -b
    a = c - a -b
    count += 1
print(c)
