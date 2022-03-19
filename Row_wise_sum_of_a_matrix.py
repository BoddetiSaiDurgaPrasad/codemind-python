a,b=map(int,input().split())
c=[]
for i in range(a):
    k=list(map(int,input().split()))
    c.append(sum(k))
print(*c)