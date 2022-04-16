def prime(n):
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    return True
n=int(input())
k=str(n)
k=k[::-1]
k=int(k)
if(prime(n)==True and prime(k)==True):
    print("circular prime")
elif(prime(n)==True and prime(k)==False):
    print("prime but not a circular prime")
else:
    print("not prime")