n=int(input())
c=[]
k=list(map(int,input().split()))
a,b=map(int,input().split())
for i in range(len(k)):
    if(a<=k[i] and k[i]<=b):
        c.append(k[i])
#print(c)
if(len(c)>=2):
    print(*(c))
else:
    print(-1)