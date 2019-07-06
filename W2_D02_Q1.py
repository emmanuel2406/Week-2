array = input("Input the marbles:")
output = ''
count = len(array)
while count != 0:
    mx = "0"
    for char in array:
        if array.count(char) > array.count(mx) and char not in output:
            mx = char
    output += (mx * array.count(mx))
    count -= array.count(mx)
print(output)
            
