def fac(n):
    c=0
    for i in range(1,n//2+1):
        if(n%i==0):
            c+=i
    return c
n=int(input())
k=fac(n)
if(k>n):
    print("True")
else:
    print("False")