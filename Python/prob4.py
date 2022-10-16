import time

def palindrome(min,max):
    b = ''
    c = ''
    palindromeList = []
    
    for i in range (min,max):
        for j in range (min,max):
            b = str(i*j)
            c = b[::-1]
            if c == b:
                palindromeList.append(int(b))
    palindromeList.sort()
    return (print(palindromeList[-1]))

timeStart = time.time()
palindrome(1000,10000)
timeEnd = time.time()
print(f'the program ran in {timeEnd-timeStart} sec')

