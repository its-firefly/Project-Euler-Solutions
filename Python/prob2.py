def fibonacci(n):
    fib = [1,2]
    sum = 0
       
    while fib[-1]<n:
        fib.append(fib[-1]+fib[-2])
    
    fib.pop(-1)
    
    for i in fib:
        if i%2 == 0:
            sum+=i
        
    return print(sum)
        
fibonacci(4000000)