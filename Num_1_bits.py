def numbit_1(n):
    binary=bin(n)
    count =0
    while n != 0:
        n= n & (n-1)
        count +=1
    return f"Binary = {binary} ; Count of 1's = {count}"