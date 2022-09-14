def ispal(n):
    n=str(n)
    c=n
    c=c[::-1]
    return c==n
n=int(input())
c=0
k=0
for i in range(n-1,n-100,-1):
    if(ispal(i)):
        c=i
        break
for i in range(n+1,n+100):
    if(ispal(i)):
        k=i
        break
if(abs(c-n)==abs(k-n)):
    print(c,k)
elif(abs(c-n)>abs(k-n)):
    print(k)
else:
    print(c)
    