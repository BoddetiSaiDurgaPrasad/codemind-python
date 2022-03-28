def prime(n):
    if(n==0 or n==1):
        return False
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    return True
n=int(input())
c=[]
for i in range(n-10,n+10):
    if(prime(i)==True):
        c.append(abs(n-i))
print(min(c))