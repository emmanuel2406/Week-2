n = int(input())
output = 0
for num in range(1,n//2 + 1):
    if n % num == 0:
        output += num 
print(output)
