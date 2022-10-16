def diff(n):
    sum = 0
    sqSum = 0   

    for i in range(1,n+1):
        sqSum += i*i
        sum += i
        
    return(print((sum*sum)-sqSum))

diff(100)




