n=int(input())
s=list(map(int,input().split()))
e=set(s)
e=list(e)
c=0
for i in range(len(e)):
    if(e[i]%2!=0 ):
        c+=e[i]
print(c)