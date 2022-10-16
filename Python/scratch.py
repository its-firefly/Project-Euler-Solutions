#num = 8
num = 88
num2 = 600851475143
a = 0
b = []
c = 0
d = []

# factorisation code





#prime check code
for i in range (1,num+1):
    if num%i == 0:
        a+=1
        b.append(i)

for j in range (len(b)):
    for k in range (1,b[j]+1):
        if b[j]%k == 0:
            c += 1
            if c == 2:
                d.append(b[j])



if a == 2:
    print(f'the {num} is a prime number')

else:
    print(f'the {num} is not a prime')

print (b)
print (d)
