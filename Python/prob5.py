def smallestMultiple(n):
    multiple = 0
    
    for j in range (1, 10000):
        for i in range (1,n+1):
            if j%i == 0:
                multiple = j
    return print(multiple)

smallestMultiple(10)

