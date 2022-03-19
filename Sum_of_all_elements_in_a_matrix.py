a,b=map(int,input().split())
c=0
for i in range(a):
    k=list(map(int,input().split()))
    c+=sum(k)
print(c)