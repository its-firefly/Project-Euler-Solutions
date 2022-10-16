def multiples(n):
    
    factors = []
    for i in range (1,n):
        if i%3 == 0 or i%5 == 0:
            factors.append(i)
    
    return(sum(factors))


print(multiples(1000))
