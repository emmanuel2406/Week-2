def is_power_of_2(n):
    while n >1:
        n = n/2
    if n == 1:
        return 1
    else:
        return 0
