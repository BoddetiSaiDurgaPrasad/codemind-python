n=int(input())
s=list(map(int,input().split()))
b=int(input())
a=set(s)
a=list(a)
c=[]
for i in range(len(a)):
    if(s.count(a[i])==b):
        c.append(a[i])
if(len(c)>=1):
    print(*c)
else:
    print(-1)