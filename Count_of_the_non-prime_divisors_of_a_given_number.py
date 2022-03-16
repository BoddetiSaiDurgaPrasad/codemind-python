def fac(n):
    c=[]
    for i in range(1,n+1):
        if(n%i==0):
            c.append(i)
    return c
def we(n):
    if(n==1 or n==0):
        return False
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    else:
        return True
n=int(input())
s=fac(n)
c=0
for i in range(len(s)):
    if(we(s[i])==False):
        c+=1
print(c)