def mul(n):
    c=0
    for i in range(1,n//2+1):
        if(n%i==0):
            c+=i
    return c
n=int(input())
m=int(input())
c1=mul(n)
c2=mul(m)
#print(c1,c2)
if(n==c2 and m==c1):
    print("Amicable")
else:
    print("Not Amicable")