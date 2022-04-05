n=int(input())
k=list(map(int,input().split()))
m=int(input())
c=[]
if(k.count(m)>=1):
    for i in range(len(k)):
        if(k[i]==m):
            c.append(i)
    print(min(c),max(c))
else:
    print(-1,-1)