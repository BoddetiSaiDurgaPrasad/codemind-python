n=int(input())
def prime(n):
    if(n==0 or n==1):
        return False
    for i in range(2,n//2+1):
        if(n%i==0):
            return False
    else:
        return True
s=str(n)
s=len(s)
if(prime(n)==True):
    c=0
    while(n!=0):
        r=n%10
        if(prime(r)==True):
            c+=1
        n=n//10
    if(c==s):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")