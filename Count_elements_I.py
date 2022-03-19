a,b=map(int,input().split())
t=list(map(int,input().split()))
u=list(map(int,input().split()))
c=t+u
c=set(c)
c=list(c)
h=0
for i in range(len(c)):
    if(t.count(c[i])>=1 and u.count(c[i])>=1):
        h+=1
print(h)