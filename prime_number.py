n=int(input())
def prime(n):
    if(n==0 or n==1):
        return False
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    else:
        return True
if(prime(n)==True):
    print("prime")
else:
    print("not a prime")