def max(array_of_numbers, len_of_array):
    output = 0
    for num in array_of_numbers:
        if num > output:
            output = num
    return output
        
    
