N  = int(input("Enter N:"))
array = []
while N != 0:
    array.append(int(input("Enter a number:")))
    N -=  1
#array = array.sort(key = int)

output_prgrsn = [0]
for a in range(0,len(array)):
    for d in range(1,max(array)):
        prgrsn = [array[a]]
        while prgrsn[-1] + d in array:
            if (int(prgrsn[-1]) + d) in array:
                prgrsn.append(int(prgrsn[-1]) + d)
        if len(prgrsn) >= len(output_prgrsn) and int(prgrsn[-1]) > int(output_prgrsn[-1]):
            output_prgrsn = prgrsn
            count = 1
        elif len(prgrsn) == len(output_prgrsn):
            count +=1
print("length of progression:",len(output_prgrsn))
print("number of progressions:", count)
print("progression first term:", output_prgrsn[0])
print("progression common difference:", (int(output_prgrsn[1]) - int(output_prgrsn[0])))
    
