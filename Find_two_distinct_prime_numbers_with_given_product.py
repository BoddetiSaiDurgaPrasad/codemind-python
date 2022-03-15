def prime(n):
    if(n==0 or n==1):
        return False
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    else:
        return True
n=int(input())
c=[]
for i in range(2,n//2+1):
    if(n%i==0):
        if(prime(i)==True):
            c.append(i)
if(len(c)<2):
    print(-1)
else:
    print(*c)